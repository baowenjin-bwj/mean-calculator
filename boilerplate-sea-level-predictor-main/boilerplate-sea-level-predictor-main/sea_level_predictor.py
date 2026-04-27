import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. 读取数据
    df = pd.read_csv('epa-sea-level.csv')

    # 2. 创建散点图
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # 3. 对所有数据进行线性回归并绘制预测线（1880-2050）
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, intercept + slope * years_extended, 'r', label='All data line of best fit')

    # 4. 仅使用2000年及以后的数据进行线性回归并绘制预测线（2000-2050）
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = pd.Series(range(2000, 2051))
    plt.plot(years_recent_extended, intercept_recent + slope_recent * years_recent_extended, 'g', label='2000+ line of best fit')

    # 5. 设置图表标签和标题
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # 保存图片并返回
    plt.savefig('sea_level_plot.png')
    return plt.gca()
