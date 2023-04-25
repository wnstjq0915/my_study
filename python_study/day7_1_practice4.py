"""
다음 함수를 정의하세요.
정수 n을 입력받고, n보다
작은 수 중 3의 배수와
5의 배수를 모두 더한 합을
반환하는 함수
함수 이름: sum_3
""" # 만약 실제 상황이면 음수 포함인지도 확인하기
# while문
# def sum_3(n):
#     answer = 0
#     while n > 2:
#         n -= 1
#         if n % 3 == 0 or n % 5 == 0:
#             answer += n
#     return answer
# print(sum_3(int(input("정수: "))))


# for문
# def sum_3(n):
#     answer = 0
#     for i in range(3, n): # range(n) 도 가능
#         if i % 3 == 0 or i % 5 == 0:
#             answer += i
#     return answer
# print(sum_3(int(input("정수: "))))


"""
정육면체 주사위 2개가 있다.
2개의 주사위를 던졌을 때
나올 수 있는 주사위 눈의 조합을
모두 print하는 함수를 정의하세요.
함수 이름: draw_dice
"""
# 조합을 모두 프린트하는 것이기 때문에 매개변수가 없어도 됨.
# 리턴값 없고 프린트하는 함수

# 2중 for문이 가장 간단, while문도 가능은 하나 조금 번거로워지고 수정이 힘듬.
# 구구단이랑 같은 방식으로 하면 쉬움

# def draw_dice():
#     dice = [1, 2, 3, 4, 5, 6]
#     for i in dice:
#         for j in dice:
#             print(f"{i}, {j}")
# draw_dice()


# # while문. 둘 다 할 수 있어야됨.
# def draw_dice():
#     i = 1
#     while i < 7:
#         j = 1
#         while j < 7:
#             print(i, j)
#             j += 1
#         i += 1

"""
두 수의 차이를 구하는 함수
함수에 입력된 두 정수의 차이를
계산하고 반환하는 함수를 정의하세요.
함수 이름: get_diff
"""
# def get_diff(n1, n2):
#     return abs(n1 - n2)
# print(get_diff(62, 25)) # 37 잘 출력


"""
가장 큰 수를 만드는 함수
함수에 입력된 5개 정수를 (0 ~ 9)(중복한 값 받기 가능)
사용하여 만들 수 있는 가장 큰
수를 반환한는 함수를 정의하세요.
함수 이름: get_biggest
""" # 정수 5개를 나열해서 가장 큰 값 만들기


# # # 문제를 잘못 이해하고 사칙연산해서 가장 큰 값 만듦.
# def get_biggest(n1, n2, n3, n4, n5):
#     result = 0
#     a = [n1, n2, n3, n4, n5]
#     while a.count(0) >= 1: # 리스트에서 0 없애기
#         a.remove(0)
#     while a.count(1) >= 1: # 리스트에서 1이 나올 경우 결과값에 1 더하기
#         result += 1
#         a.remove(1)
#     if result < 2 and len(a) != 0: # 결과값이 2보다 작거나 리스트의 길이가 0일 경우
#         result += min(a) # 리스트 안의 최솟값을 결과값에 더하기
#         a.remove(min(a))
#     if len(a) == 0: # 리스트 길이가 0일경우 결과 리턴
#         return result
#     a.sort()
#     for i in a:
#         result *= i
#     return result
# print(get_biggest(0, 1, 2, 3, 4)) # 36으로 잘 출력됨


# def get_biggest(a, b, c, d, e):
#     result = ""
#     list_num = [a, b, c, d, e]
#     list_num.sort(reverse = True)
#     for i in list_num: # for문 말고 map을 쓰면 편함
#         result += str(i)
#     return int(result)
# print(get_biggest(0, 1, 2, 3, 4)) # 잘 출력됨


# join 함수를 썼을 경우
# def get_biggest(a, b, c, d, e):
#     result = ""
#     list_num = [str(a), str(b), str(c), str(d), str(e)]
#     list_num.sort(reverse = True)
#     result = ''.join(list_num)
#     return int(result)
# print(get_biggest(0, 1, 2, 3, 4)) # 잘 출력됨


# 문자열을 안 쓰는 방법도 있음
# result = 0으로 하고
# for i in range(len(list_num)):
#     result += numbers[i] * (10 ** i)
# return result
# 이렇게 자릿수 늘리면서 넣는 것도 가능


"""
별 찍기2
정수를 함수에 입력하여
호출하면 해당 정수 줄의
별을 화면에 출력한다.
함수 이름: print_stars2
"""
# def print_stars2(n):
#     for i in range(1, n + 1):
#         print(" " * (n - i) + "*" * i)
# print_stars2(5) # 잘 나옴.