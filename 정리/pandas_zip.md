# pandas 모음
- import pandas as pd


# pandas 특성
- 인덱싱 방식
```python
obj = pd.Series([0, 1, 2, 3, 4, 5, 6, 7], index['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], dtype='int64') # 생성
"""
obj
a    0
b    1
c    2
d    3
e    4
f    5
g    6
h    7
"""
obj[3] # 3
obj[-1] # -7
obj[[1,3,5]] #multi index 접근방법
# b 1
# d 3
# f 5
obj[1:3]
# b 1
# c 2
obj[obj<3] # boolean indexing
# a 0
# b 1
# c 2
obj.c # 2
obj['c'] # 2
obj[['e','c']]
# e 4
# c 2
obj['a':'c']
# a 0
# b 1
# c 2
obj['d':'e']=100 # 슬라이싱으로 값 변경 가능. d, e에 대응되는 값이 100으로 변경.
```
