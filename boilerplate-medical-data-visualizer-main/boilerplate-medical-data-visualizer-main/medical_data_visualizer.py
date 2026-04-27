import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. 读取数据
df = pd.read_csv('medical_examination.csv')

# 2. 添加 overweight 列（BMI>25 为 1，否则为0）
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. 标准化 cholesterol 和 gluc（>1 为 1，否则为0）
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. 绘制分类图
def draw_cat_plot():
    # 准备数据
    df_cat = pd.melt(df, 
                     id_vars=['cardio'],
                     value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # 绘制计数图
    fig = sns.catplot(x="variable", hue="value", col="cardio",
                      data=df_cat, kind="count", height=6, aspect=.75)
    fig.set_ylabels('total')
    fig.savefig('catplot.png')
    return fig

# 5. 绘制热力图
def draw_heat_map():
    # 数据清洗
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 计算相关矩阵
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 绘制热力图
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', linewidths=.5, cmap='coolwarm')
    fig.savefig('heatmap.png')
    return fig

# 运行绘图
draw_cat_plot()
draw_heat_map()
