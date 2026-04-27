import pandas as pd

def calculate_demographic_data(print_data=True):
    # 读取数据
    df = pd.read_csv('adult.data.csv')

    # 1. 种族分布统计
    race_count = df['race'].value_counts()

    # 2. 男性平均年龄
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. 拥有学士学位的人口比例
    percentage_bachelors = round(df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100, 1)

    # 4. 高学历人群中收入>50k的比例
    advanced_edu = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(advanced_edu)]
    lower_education = df[~df['education'].isin(advanced_edu)]

    higher_education_rich = round(higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0] * 100, 1)
    lower_education_rich = round(lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0] * 100, 1)

    # 5. 每周工作时长最少的人里，高收入比例
    min_work_hours = df['hours-per-week'].min()
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(min_workers[min_workers['salary'] == '>50K'].shape[0] / min_workers.shape[0] * 100, 1)

    # 6. 高收入比例最高的国家
    country_rich_ratio = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100).dropna()
    highest_earning_country = country_rich_ratio.idxmax()
    highest_earning_country_percentage = round(country_rich_ratio.max(), 1)

    # 7. 印度高收入人群的热门职业
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # 打印结果
    if print_data:
        print("每个种族的人数:\n", race_count)
        print("男性的平均年龄:", average_age_men)
        print("拥有学士学位的人口比例:", percentage_bachelors)
        print("高学历人群中收入>50k的比例:", higher_education_rich)
        print("低学历人群中收入>50k的比例:", lower_education_rich)
        print("每周最少工作时长:", min_work_hours)
        print("每周工作时长最少的人中高收入比例:", rich_percentage)
        print("高收入比例最高的国家:", highest_earning_country, highest_earning_country_percentage)
        print("印度高收入人群的热门职业:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
