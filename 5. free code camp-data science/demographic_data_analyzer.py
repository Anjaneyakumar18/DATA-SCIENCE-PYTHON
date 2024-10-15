import pandas as pd

def demographic_data_analyzer(df):
       # Read the data from CSV
    df = pd.read_csv('adult.data.csv')

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    # 4. What percentage of people with advanced education (Bachelors, Masters, Doctorate) make more than 50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = (df[higher_education & (df['salary'] == '>50K')].shape[0] / df[higher_education].shape[0]) * 100

    # 5. What percentage of people without advanced education make more than 50K?
    lower_education = ~higher_education
    lower_education_rich = (df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_salary_stats = df[df['salary'] == '>50K'].groupby('native-country').size() / df.groupby('native-country').size() * 100
    highest_earning_country = country_salary_stats.idxmax()
    highest_earning_country_percentage = country_salary_stats.max()

    # 9. Identify the most popular occupation for those who earn >50K in India.
    india_occupations = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts()
    top_IN_occupation = india_occupations.idxmax()

    # Return all of the values
    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }

demographic_data_analyzer(pd.read_csv('''url'''))