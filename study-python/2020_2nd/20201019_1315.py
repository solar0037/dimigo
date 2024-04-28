#20201019_1315.py

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

ch1315['order_id'] = ch1315['order_id'].astype(str)  # 수치데이터 -> 문자데이터
ch1315['item_price'] = ch1315['item_price'].apply(lambda x: float(x[1:]))

# 가장 비싼 주문에서 메뉴를 몇개 주문했는가?
print(ch1315.groupby('order_id').sum()
      .sort_values(by='item_price', ascending=False)[:10])
# 특정 메뉴가 몇번 주문 되었는지 확인하기!
print(ch1315['item_name'].unique())
ch1315_select = ch1315[ch1315['item_name'] == 'Chicken Salad']
ch1315_select = ch1315_select.drop_duplicates(['item_name', 'order_id'])
print(len(ch1315_select))
print(ch1315_select.head(10))

# 특정 메뉴가 2번 이상 주문한 주문 횟수 구하기!
ch1315_select2 = ch1315[ch1315['item_name'] == 'Chicken Salad']
ch1315_select2_ordersum = ch1315_select2.groupby('order_id').sum()['quantity']
ch1315_select2_result = ch1315_select2_ordersum[ch1315_select2_ordersum >= 2]
print(len(ch1315_select2_result))
print(ch1315_select2_ordersum.head(10))
