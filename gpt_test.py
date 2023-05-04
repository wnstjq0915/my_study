import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # 3열 3행

# # axis=0을 기준으로 합계를 구합니다.
# sum_axis0 = np.sum(arr, axis=0)
# print(sum_axis0)  # 출력: [12 15 18]

# # axis=1을 기준으로 합계를 구합니다.
# sum_axis1 = np.sum(arr, axis=1)
# print(sum_axis1)  # 출력: [ 6 15 24]


# 2차원에서는 
# axis=0은 열끼리 진행(세로로만), 
# axis=1은 행끼리(가로로만) 진행


c = np.array([[0,1,2],[3,4,5]])
d = np.array([[6,7,8],[9,10,11]])

print(np.concatenate((c,d),axis=0))

# axis0
# [[ 0  1  2]
# [ 3  4  5]
# [ 6  7  8]
# [ 9 10 11]]

# axis1
# [[ 0  1  2  6  7  8]
# [ 3  4  5  9 10 11]]