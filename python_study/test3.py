# print_add(3, 5)

# def add(a, b):
#     return a + b

# def print_add(a, b):
#     print(a + b)

# 파이썬은 함수 호이스팅 불가능.
# print(a) 에러뜸. 파이썬도 지역변수개념 적용

# a = 1
# if a == 1:
#     b = 2
# print(b)
# # if는 지역변수?, 전역변수?

# a = 1
# b = 2
# a, b = b, a
# print(a, b)

# def test_func(x, test[]): # 에러
#     print(x, test)
# test_func(1, [1, 2, 3])

# for i in range(3, 0): # 앞의 값이 더 크더라도 에러는 나지 않음. 실행은 안 됨.
#     print(i)

# i = int(input("정수: "))
# if i % 3 or i % 5 == 0: # i % 5 == 0 만 적용됨.
#     print(f"{i} = 3의 배수거나 5의 배수")

# a = [1, 2, 3, 4, 5]
# print(len(a)) # 리스트 길이 5 출력

# a = []
# print(min(a)) # 리스트 안에 값이 없으면 min은 에러