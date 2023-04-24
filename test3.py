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

a = 1
b = 2
a, b = b, a
print(a, b)