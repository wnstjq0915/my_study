# 27433
# https://www.acmicpc.net/problem/27433

def recursion(n):
    if n <= 1:
        return 1
    return recursion(n-1) * n
num = int(input())
print(recursion(num))