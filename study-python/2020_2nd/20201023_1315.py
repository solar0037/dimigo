# 20201023_1315.py

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

wp1315: pd.DataFrame = pd.read_csv('http://jhserver.dimigo.hs.kr/drinks.csv')

# 1. 다음 데이터셋에서 결측값이 존재하는 컬럼은 무엇이며
# 결측값은 몇개입니까?
# 2. 다음 데이터셋에서 기초통계량을 산출할 때 통계량이 산출되는
# 컬럼은 몇 개입니까?

print(wp1315.info())
print(wp1315.describe())

# 상관계수(단일상관분석 / 다중상관분석)
corr1 = wp1315[['beer_servings', 'wine_servings']] \
.corr(method='pearson')
print(corr1)

cols = ['beer_servings', 'spirit_servings', 'wine_servings' ,'total_litres_of_pure_alcohol']
corr2 = wp1315[cols].corr(method='pearson')
print(corr2)
# 그래프 heatmap vs pairplot
cols_view = ['beer', 'spirit', 'wine', 'alcohol']
sns.set(font_scale=1.5)
hm = sns.heatmap(corr2.values, cbar=True, annot=True, square=True,
    fmt='.2f', annot_kws={'size': 15},
    yticklabels=cols_view,
    xticklabels=cols_view, cmap='BuGn')
plt.tight_layout()
plt.show()

# pairplot() 산점도 그래프
sns.set(style='whitegrid', context='notebook')
sns.pairplot(wp1315[['beer_servings', 'spirit_servings', 'wine_servings' ,'total_litres_of_pure_alcohol']], height=2.5)
plt.show()

p1315 = sns.load_dataset('penguins')
sns.pairplot(p1315, hue='species', palette='hsv')
plt.show()
