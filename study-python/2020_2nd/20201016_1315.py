# 20201016_1315.py

# 데이터분석
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 데이터 읽고 확인하기
ch1315: pd.DataFrame = pd.read_csv('http://jhserver.dimigo.hs.kr/chipotle.tsv', sep='\t')
# tsv: 구분자 tab / csv: 구분자 ,
pd.set_option('display.max_columns', 10)
print(ch1315.info())  # 결측값 확인, 데이터형태

# value_counts() vs unique() 차이점
print(ch1315['item_name'].value_counts())  # 데이터범주 + 개수
print(type(ch1315['item_name'].value_counts()))  # Series
print(ch1315['item_name'].unique())  # 중복값 제거한 데이터범주
print(type(ch1315['item_name'].unique()))  # ndarray

# Series
p1 = pd.Series([1, 2, 3])
print(p1)
print(p1.index.tolist())
print(p1.values.tolist())

ch1315['order_id'] = ch1315['order_id'].astype(str)  # 수치데이터 -> 문자데이터
ch1315['item_price'] = ch1315['item_price'].apply(lambda x: float(x[1:]))
# print(ch1315.info())
# 주문당 평균금액 출력
print(ch1315.groupby('order_id')['item_price'])
print(ch1315.groupby('order_id')['item_price'].sum())
print(ch1315.groupby('order_id')['item_price'].sum().mean())

# 한 주문당 10달러 이상 지불한 주문번호 출력
orderid_group = ch1315.groupby('order_id').sum()
print(orderid_group)
result = orderid_group[orderid_group.item_price >= 10]  #
print(result[:10]) 
print(result.index.values)

# 각 메뉴의 가격 구하기  # 50개 메뉴
item_one = ch1315[ch1315.quantity == 1]
price_per_item = item_one.groupby('item_name').min()
print(price_per_item.sort_values(by='item_price', ascending=False))

# 시각화
item_name_list = price_per_item.index.tolist()
x_pos = np.arange(len(item_name_list))  # 메뉴이름이 너무 길어서 표현이 불가
item_price = price_per_item['item_price'].tolist()
# x, y축의 값을 나타내는 것
# 그래프 그리기
plt.bar(x_pos, item_price, align='center')
# plt.plot([1, 2, 3], [4, 5, 6])
plt.ylabel('ordered_item_count')
plt.title('Distribution of item price')

plt.show()

plt.hist(item_price)

plt.ylabel('count')
plt.title('Histogram of item')
plt.show()

# 막대그래프에서 x축과 y축을 바꾸어서 출력해서 가로로 변경하여 출력하세요.
plt.barh(x_pos, item_price, align='center')
plt.xlabel('orderd_item_count')
plt.title('Distribution of item price')
plt.show()
