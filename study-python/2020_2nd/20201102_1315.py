# 20201102_1315.py 사호준

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 10)
wp1315 = pd.read_csv('http://jhserver.dimigo.hs.kr/drinks.csv')
print(wp1315.info())
# heatmap() / pairplot()
# 결측데이터 보정하기
wp1315.to_csv('wp1315_d.csv')  # 현재 DataFrame을 csv파일로 변경
wp1315['continent'] = wp1315['continent'].fillna('EXT')  # fillna('대체값'): 결측값 보정
# wp1315['continent'] => Series
print(wp1315.head(10))
wp1315.to_csv('wp1315_d.csv')  # 현재 DataFrame을 csv파일로 변경

# 파이차트 생성하기
labels = wp1315['continent'].value_counts().index.tolist()
fr1315 = wp1315['continent'].value_counts().values.tolist()
print(wp1315['continent'].value_counts())
explode = (0, 0, 0, 0.25, 0, 0)
# labels vs fr1315
print(labels, fr1315)

# plt.pie(fr1315, explode=explode, labels=labels, autopct="%.0f", shadow=True)
# plt.title('null data to \'EXT\'')
# plt.show()

# q: 대륙별 spirit_servings의 통계를 출력하세요.(Mean, Max, Min, sum)
print(wp1315['spirit_servings'].describe())
result = wp1315.groupby('continent').spirit_servings.agg(['mean', 'min', 'max', 'sum'])
print(result)
# agg: apply() 비슷한데 차이는 다중함수를 적용시킬 수 있음.
result1 = wp1315.groupby('continent').wine_servings.agg(['mean', 'min', 'max', 'sum'])
print(result1)

# Q: 전체평균보다 많은 알코올을 섭취하는 대륙은 어디일까요?
total_mean = wp1315.total_litres_of_pure_alcohol.mean()
continent_mean = wp1315.groupby('continent')['total_litres_of_pure_alcohol'].mean()
continent_over_mean = continent_mean[continent_mean>=total_mean]
print(continent_over_mean)

# Q: 평균 beer_servinngs가 가장 높은 대륙은 어디일까요?
result3 = wp1315.groupby('continent')['beer_servings'].agg(['mean'])
print(result3)
result4 = wp1315.groupby('continent')['beer_servings'].mean()
print(result4)
result5 = wp1315.groupby('continent')['beer_servings'].mean().idxmax()
# idxmax() 시리즈에서 값이 가장 큰 index 반환
print(result5)

# 시각화 꾸미기
# 대륙별 spirit_servings의 평균, 최소, 최대, 합을 시각화
n_groups=len(result.index)
means = result['mean'].tolist()
mins = result['min'].tolist()
maxs = result['max'].tolist()
sums = result['sum'].tolist()
index = np.arange(n_groups)
bar_width = 0.1
rects1 = plt.bar(index, means, bar_width, color='r',label='Mean')
rects2 = plt.bar(index + bar_width, mins, bar_width,color='g',label='Min')
rects3 = plt.bar(index + bar_width * 2, maxs, bar_width,color='b',label='Max')
rects3 = plt.bar(index + bar_width * 3, sums, bar_width,color='y',label='Sum')
plt.xticks(index, result.index.tolist())
plt.legend()
plt.show()

# Homework: 대륙별 wine_servings의 평균, 최소, 최대, 합을 시각화
result = wp1315.groupby('continent')['wine_servings'].agg(['mean', 'min', 'max', 'sum'])
n_groups=len(result.index)
means = result['mean'].tolist()
mins = result['min'].tolist()
maxs = result['max'].tolist()
sums = result['sum'].tolist()
index = np.arange(n_groups)
bar_width = 0.1
rects1 = plt.bar(index, means, bar_width, color='r',label='Mean')
rects2 = plt.bar(index + bar_width, mins, bar_width,color='g',label='Min')
rects3 = plt.bar(index + bar_width * 2, maxs, bar_width,color='b',label='Max')
rects3 = plt.bar(index + bar_width * 3, sums, bar_width,color='y',label='Sum')
plt.xticks(index, result.index.tolist())
plt.legend()
plt.show()
