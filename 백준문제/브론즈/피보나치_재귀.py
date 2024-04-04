# 10870
# https://www.acmicpc.net/problem/10870

def recursion(n):
    if n <= 1:
        return n
    return recursion(n-1) + recursion(n-2)
num = int(input())
print(recursion(num))