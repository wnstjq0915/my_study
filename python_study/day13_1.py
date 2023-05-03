# 컴퓨터는 열 위주로 생각함.
# 행렬 yx

# 1 2 3 4
# 5 6 7 8
# 15 26 37 48 이런식

# args 활용 덧셈함수 만들기
# def add_all(*args):
#     s = 0
#     for i in range(len(args)):
#         if type(args[i]) == list:
#             s += sum(args[i])
#         else:
#             s += args[i]
#     return s
# print(add_all(1, 2, 3, 4, 5))
# print(add_all([1, 2, 3], 4, 5, 6))
# print(add_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# import numpy as np
# A = [1, 2, 3, 4]
# a = np.array(A)
# s = a[:2]
# print(f"A: {A}")
# print(f"a: {a}") # array([1, 2, 3, 4])
# print(f"s: {s}")

# print(f"A: {type(A)}") # 리스트
# print(f"a: {type(a)}") # 넘피
# print(f"s: {type(s)}") # 넘피

# # 넘피는 얕은복사 깊은복사가 없는듯
# ss = a[:2].copy()
# print(ss)
# a[0] = 99
# print(ss)
# a[0] = 1
# ss = np.array(a[:2])
# a[0] = 99
# print(ss)
# # print(ss.size)
# a[0] = 1
# ss = np.array(a)
# a[0] = 99
# print(ss)

# # 브로드캐스팅
# # 다른 모양의 배열 간의 산술 연산을 수행할 수 있도록
# # 해주는 numpy의 기능
# print(a + 3) # 모든 항에 +3을 다 적용

# arr = np.zeros((3, 2)) # 3행 2열 제로스
# print(arr)

# arr.flatten() # 1d vector로 만드는 것.
# arr = np.array([[1, 2], [3, 4]])
# print(arr.flatten())
# # array([1, 2, 3, 4]) 출력

# arr = np.arange(12)
# print(arr)
# arr -> 0 ~ 11
# print(arr.reshape(3, 4)) # 주어진 shape의 약수로 이루어진 shaple만 가능
# print(arr.reshape(4, 3))
# print(arr.reshape(1, 12)) # = flatten
# print(arr.reshape(2, 6))
# print(arr.reshape(6, 2)) # 6행 2열
# arr = np.arange(20)
# print(arr)

# print(arr.reshape(-1, 5))
# print(arr.reshape(-1, 5))
# print(arr.reshape(-1, 5))
# print(arr.reshape(-1, 10)) # 앞에 -1?

# arr = np.arange(20)
# print(arr.transpose().shape)

# arr = np.arange(20).reshape(4, 5) # 4행 5열을
# print(arr.transpose().shape) # 5행 4열로


# A = [5, 23, 2, 1, 5]
# A.sort() # A가 바뀜.
# print(A)

# a = [5, 23, 2, 1, 5]
# sorted(a) # 리턴값이 없기에 a가 안 바뀜.
# print(a)

# arr = np.arange(30).reshape(3, 2, 5)
# print(arr.shape)

# arr.transpose().shape

# transpose와 같은 역할을 하는 T 사용할 예정

# x = np.arange(6).reshape(-1,3)
# print(x)
# [0 1 2][3 4 5]
# T opera
# print(x.T)
# [0 3][1 4][2 5]
# array([[0, 3], [1, 4], [2, 5]])

# arr = np.arange(20).reshape(-1, 2)
# arr1 = arr.T[0]
# arr2 = arr.T[1]
# print(arr1) # 20을 추가해야 함.
# print(arr2)


# # 넘피특성 미활용
# import numpy as np

# arr = np.arange(0,21)
# arr1 = []
# arr2 = []
# for i in arr:
#     if arr[i] %2==0:
#         arr1.append(arr[i])
#     else:
#         arr2.append(arr[i])

# import numpy as np
# Arr = np.arange(0,21)

# 0 ~ 20까지 생성해서 홀수 짝수 각각 다른 변수에 담기 답:
# Arr1 = Arr[Arr%2==0] # arr의 0~20값을 하나하나 짝수인지 확인해서 추가
# Arr2 = Arr[Arr%2!=0]
# print(Arr1)
# print(Arr2)

# [1, 2, 3, 4, 5][2:4] = 1
# 리스트는 슬라이싱 범위 내를 1로 바꿀 수 없음

# arr1 = np.arange(8)
# arr1[3:6] = 100 # 넘피는 슬라이싱 범위에 한번에 할당 가능
# print(arr1)

# view
# arr2 = np.arange(20).reshape(4, -1)
# print(arr2)
# print(arr2[0]) # 첫번째 행
# print(arr2[1][2]) # 재귀적 접근 / 1행 2열
# print(arr2[1, 2]) # 컴마를 통해 쉬운 인덱싱 가능

# arr3 = np.arange(20).reshape(4, -1)
# print(arr3)
# # arr3[:3][:2]
# # array([[0, 1, 2, 3, 4],
#     #    [5, 6, 7, 8, 9]])
# # 행과 열을 접근하기 위해서는 컴마로 연결해야 함.
# print(arr3[:3, :2])

# # 불리안 배열.
# arr = np.array([0, 1, 2, 3, 4])
# arr[[True,False,True,False,True]]
# # 프린트하면 array([0, 2, 4]) 출력

# arr2 = np.arange(20).reshape(4,5)
# print(arr2)
# print(arr2[[0,2]]) # 0행과 2행 # multi index(여러개 인덱스)는 []하나 더 추가해야 함.

# print(arr2[[0,3], [4]]) # 인덱스 0행과 3행에서 4번 인덱스 가져오기
# print(arr2[0,4]) # 하나만 가져오는건 전과 같이 [] 하나만

# import numpy as np

# 유니버설 함수
# arr = np.arange(-3, 3).reshape(3, -1)
# print(arr)

# e에 몇제곱을 하든 2.7xxxx값
# np.floor(arr) -> 소수점 버리기
# 이항 유니버설 함수.

# arr1 = np.arange(8).reshape(2, -1)
# arr2 = np.arange(-40, 40, 10).reshape(2, -1)
# print(arr1)
# [[0 1 2 3]
# [4 5 6 7]]

# print(arr2)
# [[-40 -30 -20 -10]
# [0 10 20 30]]


# print(np.maximum(arr1, arr2)) # 같은 원소에서 가장 큰 값.
# [[0 1 2 3]
# [4 10 20 30]]

# print(np.subtract(arr1, arr2)) # 뺄셈
# [[ 40  31  22  13]
#  [  4  -5 -14 -23]]

# np.multiply(arr1,arr2) #같은 원소끼리 곱셈.


# 통계 메서드
# arr = np.arange(4).reshape(2,2)
# print(arr.sum())
# print(arr.sum(axis=0)) # [2 4]
# print(arr.sum(axis=1)) # [1 5]

# print(arr.mean(axis=0))
# # [1. 2.]
# 왜 정수가 float의 . 형태로 나타나는지.
# 표현할 수 있는 범위가 float이 넓기 때문에 float 처리

# print(arr.mean(axis=1))
# # [0.5 2.5]


# where
# x if 조건 else y의 백터화 버전
# numpy를 사용하여 배열을 빠르게 처리 할 수 있으며,
# 다차원도 간결하게 표현 가능

# xarr = np.array([100,200,300,400])
# yarr = np.array([1,2,3,4])
# cond = np.array([True,False,True,False])
# result = np.where(cond,xarr,yarr)
# 트루면 x어레이, false면 y어레이
# print(result) # [100   2 300   4]

# np.where(xarr>200,max(xarr,0))
# np.where(xarr%3==0,1,0)


# # sort()
# np.random.seed(42)
# arr = np.random.randint(1,100,size=10) #1~100까지의 정수중에 10개를 뽑아주세요.
# print(arr)
# print(-arr) # arr값이 음수화돼서 나옴
# print(np.sort(arr)) # 오름차순
# print(-np.sort(-arr)) # 내림차순
# array의 sort는 내림차순, 오름차순을 선택하는 옵션이 없다.


# 선형대수 패키지
# 단위행렬
# 대각 원소 1이고, 나머지는 0인 n차 정방행렬을 말하며,
# numpy의 eye()함수를 사용하여서 만들 수 있음.

import numpy as np
# identity = np.eye(4)
# print(identity)

# identity = np.eye(2, 3)
# print(identity)


# 대각행렬
# 대각성분 이외의 모든 성분이 모든 성분이
# 모두 '0'인 n차 정방행렬을 말함.

# x = np.arange(9).reshape(3,-1)
# print(x)

# print(np.diag(x)) #diagonal matrix

# print(np.diag(np.diag(x)))


# dot
# 벡터의 내적, 원소간의 곱(element-wise product)
# 벡터의 내적.(행렬의 곱)

# a = np.arange(4).reshape(-1, 2)
# print(a)
# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print(a*a) # dot product
# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print(np.multiply(a,a))
# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print(np.dot(a,a)) # 행렬의 곱
# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print(a.dot(a))


# matmul: matrix multiplication
a = np.random.randint(-3,3,10).reshape(2,5)
b = np.random.randint(0,5,15).reshape(5,3)
print(a.shape,b.shape)
# print(a) # 랜덤한 2, 5 행렬
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print(b) # 랜덤한 5, 3 행렬
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
ab = np.matmul(a,b)
print(ab.shape,'\n') #\n : 개행
print(ab)

# ba = np.matmul(b,a) # 자릿수가 맞아야됨
# ab = np.matmul(a,b.T) # 자릿수가 맞아야됨


# np.dot(a, b) # dot -> 1차원 벡터 공식문서에는 2d matmul로 돌아감
# 벡터를 곱했다 -> 내적