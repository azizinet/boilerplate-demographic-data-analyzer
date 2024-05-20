import numpy as np
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.value_counts(subset = ['race'])

    # What is the average age of men?
    average_age_men = np.round(df.loc[df['sex'] == 'Male', 'age'].mean(), decimals = 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = np.round(len(df.loc[df['education'] == 'Bachelors']) * 100 / len(df), decimals = 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[df.education.isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df.loc[~df.education.isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = np.round(len(higher_education.loc[higher_education['salary'] == '>50K']) * 100 / len(higher_education), decimals = 1)
    lower_education_rich = np.round(len(lower_education.loc[lower_education['salary'] == '>50K']) * 100 / len(lower_education), decimals = 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]

    rich_percentage = np.round(len(num_min_workers.loc[num_min_workers['salary'] == '>50K']) * 100 / len(num_min_workers), decimals = 1)

    # What country has the highest percentage of people that earn >50K?
    countries = set(df['native-country'].tolist())
    country_salary_ratio = {}

    for negara in countries:
        country_salary_ratio[negara] = len(df.loc[(df['native-country'] == negara) & (df['salary'] == '>50K')]) * 100 / len(df.loc[df['native-country'] == negara])

    highest_earning_country = list(country_salary_ratio.keys())[list(country_salary_ratio.values()).index(max(country_salary_ratio.values()))]
    highest_earning_country_percentage = np.round(max(country_salary_ratio.values()), decimals = 1)

    # Identify the most popular occupation for those who earn >50K in India.
    df_India = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

    top_IN_occupation = df_India['occupation'].value_counts().index.tolist()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data()