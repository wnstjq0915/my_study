# 4779
# https://www.acmicpc.net/problem/4779
# 재귀함수를 사용하는 것이 목적

# 초기 제출안
# def func(n_str):
#     if len(n_str) % 3 != 0:
#         return '-'
#     len_str = len(n_str) // 3
#     div_str = '-' * len_str
#     return func(div_str) + ' '*len_str + func(div_str)
# while True:
#     try:
#         num = int(input())
#         print(func('-'*3**num))
#     except: break

# 최적화
def func(n):
    if n % 3 != 0:
        return '-'
    n_mul = n // 3
    return func(n_mul) + ' '*n_mul + func(n_mul)
while True:
    try:
        num = int(input())
        print(func(3**num))
    except: break