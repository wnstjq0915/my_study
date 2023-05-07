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


# c = np.array([[0,1,2],[3,4,5]])
# d = np.array([[6,7,8],[9,10,11]])

# print(np.concatenate((c,d),axis=0))

# axis0
# [[ 0  1  2]
# [ 3  4  5]
# [ 6  7  8]
# [ 9 10 11]]

# axis1
# [[ 0  1  2  6  7  8]
# [ 3  4  5  9 10 11]]


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# import numpy as np
# # a = np.array([1, 2, 3])
# # b = np.array([4, 5, 6])
# # c = np.array([7, 8, 9])
# # d = np.column_stack((a, b, c))
# # print(d)
# a = np.array([1, 2, 3, 4])

import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# print(arr.mean())  # Output: 3.0

# arr = np.array([[1, 2], [3, 4]])
# print(arr.mean(axis=0))  # Output: [2. 3.]

# arr = np.array([[1, 2], [3, 4]])
# print(arr.mean(axis=1))  # Output: [1.5 3.5]

xarr = np.array([100,200,300,400])
yarr = np.array([1,2,3,4])
cond = np.array([True,False,True,False])
print(np.where(xarr>200,max(xarr),0))