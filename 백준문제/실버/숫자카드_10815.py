def dichotomy(li, num):
    i = len(li) - 1

    while i != 0:
        if num > li[i]:
            li = li[i:]
        elif num < li[i]:
            li = li[:i+1]
        else:
            return "1"
        i = (len(li) - 1) // 2
    return "1" if li[i] == num else "0"

input()
a = list(set(map(int, input().split())))
a.sort()

input()
b = list(map(int, input().split()))

ans = ""
for num in b:
    ans += dichotomy(a, num) + " "
print(ans[:-1])