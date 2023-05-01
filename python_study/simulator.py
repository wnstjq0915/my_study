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