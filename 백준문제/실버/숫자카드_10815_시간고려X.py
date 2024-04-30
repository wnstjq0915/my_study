a = int(input())
a = list(set(map(int, input().split())))

b = int(input())
b = list(map(int, input().split()))

ans = ""
for num in b:
    ans += "1 " if a.count(num) != 0 else "0 "
print(ans[:-1])