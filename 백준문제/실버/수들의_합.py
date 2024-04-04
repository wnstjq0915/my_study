# 1789
# https://www.acmicpc.net/problem/1789

# 문제 주의해서 읽기

# 정석
# num = int(input())
# sum_num = 0
# i = 0
# while sum_num <= num:
#     i += 1
#     sum_num += i
# print(i-1)


# 근의공식 활용
num = int(input())
print(((8*num+1)**(1/2) - 1) // 2)


"""
1부터 n까지 합 s

n(1+n) / 2 >= s
2s <= n(1+n)

s = 200일 때
400 <= n^2 + n
n^2 + n - 400 >= 0
"""