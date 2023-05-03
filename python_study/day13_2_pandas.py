# Pandas
# Series
# 리스트와 딕셔너리가 섞임.

import numpy as np
import pandas as pd

# obj = pd.Series([0, 1, 2, 3, 4, 5, 6, 7], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], dtype='int64')
# # print(obj)

# # integer -location based 순서(정수)로 접근
# print(obj[3])
# print(obj[-1]) # 인덱싱, 슬라이싱 가능
# print(obj[[1, 3, 5]]) # multi index 접근방법
# print(obj[1:3])
# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print(obj[obj < 3]) # boolean indexing, 인덱스 3보다 작은 값만 가져옴.

# label location based
# print(obj)
# print(obj.c) # 딕셔너리처럼 값으로 접근 가능.
# print(obj['c']) # 위에랑 같은거
# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print(obj[['e', 'c']]) # 멀티인덱스 가능
# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print(obj['a':'d'])
# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# obj['d':'e'] = 100
# print(obj)

# obj = pd.Series([0, 1, 2, 3, 4, 5, 6, 7], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], dtype='int64')
# print(obj.iloc[2]) # 2 출력
# print(obj.iloc[[2]])
# print(obj.iloc[1:4])
# print(obj.loc['a' : 'c'])

# df = pd.DataFrame(np.arange(24).reshape(4,-1),
#                 columns = ['c1','c2','c3','c4','c5','c6'],
#                 index=['r1','r2','r3','r4'])
# print(df['c3'])
# print(df[['c1','c3']])
# print(df['r1':'r2'])
# print(df['c1':'c2'])
# print(df.iloc[[0], [3]])
# print(df.iloc[[0, 1], 1:4])
# print(df.loc[['r1'], ['c4']])
# print(df.loc['r1':'r2', ['c2', 'c3', 'c4']])
# print(df.loc['r1':'r2', ['c3', 'c4', 'c2']])

# 산술 연산자
# s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
# print(s1 + s2)

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['b', 'c', 'd', 'e'])
# print(s1 + s2) # SQL의 outer join. outer join은 합집합으로 나와서 겹치지 않아도 출력
# sql이라는 국가공인자격이 있음, 공인 쿠버네티스 자격증도 있음
print(s1.add(s2, fill_value=0))
