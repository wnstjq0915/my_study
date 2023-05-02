# a = {2, 3, 1, "hello"}
# b = {2, 'hello'}
# print(a & b)

# a = 34
# b = 4
# if a % b > 3:
#     print('실패')
# elif a % b == 3:
#     print('무승부')
# else:
#     print('성공')

# age = 2023 - int(input('태어난 년도 4자리: ')) + 1
# print(age)
# if 20 <= age <= 26:
#     print('대학생')
# elif 17 <= age <20:
#     print('고등학생')
# elif 14 <= age < 17:
#     print('중학생')
# elif 8 <= age < 14:
#     print('초등학생')
# else:
#     print('학생이 아닙니다')


# num = int(input("양의 정수: "))
# if num % 3 == 0 and num % 2 == 0:
#     print(f"{num}은 2와 3의 공배수입니다.")
# elif num % 3 == 0:
#     print(f"{num}은 3의 배수입니다.")
# elif num % 2 == 0:
#     print(f"{num}은 2의 배수입니다.")
# else:
#     print(f'{num}은 2와 3의 배수가 아닙니다.')

# for i in range(6)[::-1]:
#     print(i)

# # 같은 코드
# for i in range(5, -1, -1): # 5부터 5 직전까지(인덱스 -1은 가장 뒤에 인덱스) -1간격(거꾸로)
#     print(i)

# print(sum(range(11)))

# n = int(input("양의 정수: "))

# for i in range(n):
#     print(f"{' ' * i}*****")

# for i in range(1, n + 1):
#     print("*" * i)

# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * i)

# for i in range(n):
#     print("*" * (n - i))

# for i in range(n):
#     print(' ' * i + "*" * (n - i))

# for i in range(n):
#     print(" " * (n - 1 - i) + "*" + "*" * 2 * i)


# a = True
# print(a) # True
# a = not a
# print(a) # False
# a = not a
# print(a) # True

# x = [3, 6, 9, 20, -7, 5]
# answer = []
# for i in x:
#     print(i * 10)
#     answer.append(i * 10)
# print(answer)

# y = {"math": 70, "science": 80, "english": 20}
# for i in y.keys():
#     y[i] += 10
#     print(y[i])
# print(y)

# import random
# true_value = random.randint(1,100)
# i = 1
# while True: # while true_value != input_value:로 하고 '정답닙니다' 프린트를 while문 밖에 써도 됨.
#     input_value = int(input("1~100의 숫자를 입력해주세요: "))
#     if input_value == true_value:
#         print(f"{i}번째: 정답입니다. 입력한 숫자는 {true_value}입니다.")
#         break
#     elif input_value > true_value:
#         print(f"{i}번째: 숫자가 너무 큽니다.\n")
#     else:
#         print(f"{i}번째: 숫자가 너무 작습니다.\n")
#     i += 1

# word = ['shool', 'game', 'piano', 'science', 'hotel', 'mountain']
# answer = []
# for i in word:
#     if len(i) > 5:
#         answer.append(i)
# print(answer)

# i = 1
# num = int(input("정수: "))
# three = []
# five = []
# three_five = []
# if num < 1:
#     i = -1
# for i in range(1, num + i, i):
#     if i == 0:
#         continue
#     if i % 3 == 0 and i % 5 == 0:
#         three_five.append(i)
#     elif i % 3 == 0:
#         three.append(i)
#     elif i % 5 == 0:
#         five.append(i)
# print(f"3과 5의 공배수: {three_five}")
# print(f"3의 배수: {three}")
# print(f"5의 배수: {five}")

# b = 0
# while True:
#     a = input("정수 or s: ")
#     if a == 's' or a == 'S':
#         break
#     if a.isdecimal():
#         b += int(a)
# print(b)

# kor_score = [39, 69, 20, 100, 80]
# math_score = [32, 59, 85, 30, 90]
# eng_score = [49, 70, 48, 60, 100]
# # avg = []
# # for i, j, k in zip(kor_score, math_score, eng_score):
# #     avg.append((i + j + k) / 3)
# # print(avg)


# # 행렬 사용
# student_score = [0,0,0,0,0]
# i = 0
# midterm_score = [kor_score, math_score, eng_score]
# for subject in midterm_score: # kor, math, eng 과목 선택
#     for score in subject: # 과목 선택 후
#         student_score[i] += score # 각 학생마다 개별로 교과 점수를 저장
#         # print(subject, score, 'i:', i, student_score) # kor -> math -> eng
#         i += 1 # 학생 index 구분
#     i = 0 # 과목이 바뀔 때 학생 인덱스
# else:
#     a, b, c, d, e = student_score # 학생별 점수를 unpacking
#     student_average = [a/3, b/3, c/3, d/3, e/3]
#     print(student_average)


# def div(a, b):
#     if b == 0:
#         print("0으로 나눌 수 없습니다.")
#     elif a.isdecimal() and b.isdecimal():
#         a, b = int(a), int(b)
#         return (a // b, a % b)
#     else:
#         print("정수를 입력해주세요.")

# print(div(input("정수1: "), input("정수2: ")))


# def func(s, unit = 2):
#     i = 0
#     while i < len(s):
#         print(s[i:i + unit])
#         i += unit
# func(input("문자열: "))


# def add_all(*inputs): # 리스트를 못 받음
#     s=0
#     for i in range(len(inputs)):
#         s +=inputs[i]
#     return s

# def add_all3(*args): # 튜플을 못 받음
#     s=0
#     for i in args:
#         for j in i:
#             s +=j
#         return s

# for문 안에 if type(args[i]) == list:
# 하면 둘 다 가능

# def factor(x):
#     answer = 1
#     for i in range(1, x + 1):
#         answer *= i
#     return answer

"""
재귀적 함수
"""
#재귀적으로 하는 것.
# def fact(n):
#     if n<=1: #n이 1이하이면 종료조건
#         return 1
#     return n*fact(n-1)

# def num_list(list):
#     answer = []
#     for i, j in enumerate(list):
#         print(f"대기번호 {i + 1}번: {j}")
#         answer.append(f"{i + 1}: {j}")
#     return answer

# people = ['펭수', '뽀로로', '뚝딱이', '텔레토비']
# print(num_list(people))


# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
"""
람다
"""
# # def plus_two(num): # 이 함수를 람다 써서 만들기
# #     return num + 2

# # lambda x : x + 2 # 우리가 만들 함수
# # # <function __main__.<lambda>(x)>    -> 함수를 생성함

# func2 = lambda x : x + 2
# c = func2(2)
# print(c)

# # 람다 단점, 변수가 하나만 들어가기 때문에 map을 써야 함.

# items = [1, 2, 3, 4, 5]
# squred_map = list(map(lambda x : x ** 2, items))
# print(squred_map)

# items = [1, 2, 3, 4, 5]
# squred_map = lambda x : x ** 2
# print(list(map(squred_map, items)))

# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# items = [1, 24, 3, 6, 7]
# str_items = list(map(lambda x : str(x), items))
# print(str_items)
# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')


# """
# 0부터 9까지 순서대로 가지고 있는 리스트를 만드세요
# """
# # 1.
# list_1 = list(range(10))
# print(list_1)

"""
list comprehension
"""

# # 구구단 2단 list comprehension이랑 한줄for문으로 나타내기
# print([2 * i for i in range(1, 10)])

# # 문자열 받고 띄어쓰기 단위로 나눈 뒤 나눠진 문자열의 길이를 리스트에 저장하기
# sentence = '코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다. 외출 시에는 마스크를 끼고, 손씻기를 생활화합시다.'
# len_sent = [len(s) for s in sentence.split()]
# print(len_sent)


# # 10부터 20까지 짝수만 받기

# list3 = []
# for x in range(10, 21):
#     if x % 2 == 0:
#         list3.append(x)
# print(list3)

# list3 = list(range(10, 21, 2))
# print(list3)

"""
for문 + if문
반환할 값 for x in iterable값 if 조건

조건에 만족하는 x만 for문을 돌림.
"""
# # 1~10 수들을 제곱해서 50 이하의 숫자만 넣기
# list4 = [i ** 2 for i in range(1, 11) if i ** 2 <= 50]
# print(list4)


"""
for else if를 하나에 다 담기

if실행문 if if조건문 else else실행문 for i in iterable

if를 만족하면 앞으로, 만족하지 않으면 else값 뒤로
"""
# 1부터 10까지의 숫자들 중 홀수이면 어떤 제곱수를,
# 짝수이면 세제곱수를 담은 리스트를 만들자.

# list5 = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(1, 11)]
# print(list5)

"""
2중 for문 다 하나에 넣기
"""

# word1 = 'hello'
# word2 = 'world'
# result = [i+j for i in word1 for j in word2]
# print(result) # 앞에 for이 큰 범위, 뒤에 for이 그 안에 속함.


"""
1. 40 이하의 숫자는 5 더하고 40 초과의 숫자는 41로 바꾸어
리스트로 저장하고 출력하라.

2. 컷트라인이 60점일 때, 사람이름과 통과여부를 리스트로
담아서 출력하라. 이름과 통과여부는 튜플로 묶여있는 자료.
(이름, 통과여부)
"""

# # 2 딕셔너리 활용문제.
# # 주어진 값
# students = {
#     "보라돌이": 61, 
#     "뚜비": 35,
#     "나나": 78,
#     "뽀": 88
# }

# answer = [(i, "통과") if j >= 60 else (i, "미통과") for i, j in students.items()]
# print(answer)


# result = [(name, True) if score >= 60 else (name, False) for name, score in students.items()]
# print(result)


# import pandas as pd
# import matplotlib.pyplot as plt
# 나중에 위에 두개 쓸거


# import numpy as np
# n = 1000000
# numpy_arr = np.arange(n)
# python_list = list(range(n))

"""
주피터에서는 연산시간을 확인해볼 수 있음.

%%time
python_list = [x ** 3 + 10 for x in python_list]

%%time
numpy_arr = numpy_arr ** 3 + 10
"""
# import time

# for문이랑 numpy 속도비교

# start = time.time() # 시작시간 저장
# python_list = [x ** 3 + 10 for x in python_list]
# print('time:', time.time() - start) # 현재시각 - 시작시간 = 실행시간
# # 0.314517....

# start = time.time()
# numpy_arr = numpy_arr ** 3 + 10
# print('time:', time.time() - start)
# # 0.0040135....

# 에러
# A = [1, 2, 3, 4]
# a = np.array(A, np. int)
# print(type(a))
# print(a)

# # 백터화
# # 배열은 for문을 작성하지 않고 데이터를 일괄처리 하는 것.
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr + arr)
# print(arr / arr)

# # 브로드캐스팅
# # 다른 모양의 배열 간의 산술 연산을 수행할 수 있도록 해주는
# # numpy의 기능.

# print(10 - arr)
# print(arr * 3)
# print(arr / 3)
# arr2 = np.array([100, 200, 300])
# arr4 = np.array([[100], [200]])
# arr3 = np.array([100, 200])

# print(arr + arr2)
# list_1 = [1, 2, 3]
# print(list_1 + list_1)
# # [1, 2, 3, 1, 2, 3]

# print(arr + arr4)
# # [[101 102 103][204 205 206]]

# arr_1 = np.array([1, 2, 3])
# print(arr_1 + arr_1)
# # [2, 4, 6]

# print(arr.dtype)

# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# print(arr)
# print(arr.size) # 크기
# print(arr.ndim) # 차원
# print(arr.shape)

# import numpy as np
# # 0차원(상수)
# a = np.array(10)
# print(a)
# print(a.ndim)

# # 1차원
# a = np.array([1, 2, 3])
# print(a)
# print(a.ndim)

# # 2차원
# a = np.array([[1, 2], [3, 4]])
# print(a)
# print(a.ndim)

# # 3차원
# a = np.array([[[1, 2], [3, 4]]])
# print(a.ndim)
# print(a.shape) # 높이, 행, 열

# # range함수 이용.
# arr1 = np.array(range(20))
# # array(0, 1, 2, 3, 4, ... 19)랑 같음.

# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print(np.zeros(5))
# print(np.ones((3, 3)))
# print(np.full(4, 5))
# print(np.empty((2, 3), dtype = np.float32))
# # zeros는 0이 할당됐지만 empty는 할당이 아님. none은 값은 없지만 할당.

# print(np.arange(-3, 3))
# print(np.arange(3, 50, 3))
# print(np.linspace(0, 1, 6))

# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# # 배열 결합 함수
# # hstack, concatenate(axis = 0)
# # 두 배열을 왼쪽에서 오른쪽으로 붙이기

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# np.hstack([a, b])
# print(np.concatenate((a, b), axis=0))

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# print(np.hstack([a, b]))
# print(np.concatenate((a, b), axis=0))

# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(np.vstack([a,b]))

# # np.concatenate((a,b), axis=1) # 1D vector는 안됨.

# c = np.array([[0,1,2],[3,4,5]])
# d = np.array([[6,7,8],[9,10,11]])

# print(np.concatenate((c,d),axis=1)) # 2차원은 정상적으로 작동

# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(np.column_stack([a,b]))

import random
import numpy as np
# random.random # 0과 1 사이의 난수 리턴
# data = [1, 2, 3, 4, 5, 6, 7]
# print(np.random.choice(data, 3))

# data = ['apple','banana','grape','orange']
# print(random.choice(data))

# seed
# 난수 초기값 부여 -> 재현 가능성(Reporducibility)
# np.random.seed(42)
# print(np.random.rand(1000))


"""
로또번호 생성
1 ~ 45 6개 숫자
4번 이상 생성하기
"""
n = int(input("몇개 생성할까요: "))
arr = np.array(range(1, 46))
for i in range(1, n + 1):
    random.shuffle(arr)
    lotto_num = arr[0:6]
    lotto_num.sort()
    print(f"{i}. 로또번호: {arr[0:6]}")

# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# def make_lotto(count):
#     for i in range(count):
#         lotto_num = [] #로또 번호가 담길 리스트형 변수
#         for j in range(6): #6번 반복
#             lotto_num = np.random.choice(range(1,46),6,replace=False) # 1 ~ 45 숫자중에 6개를 뽑기 중복없이
#             lotto_num.sort() #값 정렬
#         print('{}.로또번호:{}'.format(i+1,lotto_num))

# count = int(input('로또 번호를 몇개 생성할까요?'))
# make_lotto(count)