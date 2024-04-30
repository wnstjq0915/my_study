def dichotomy(li, num):
    i = len(li) - 1

    while i != 0:
        if num > li[i]:
            li = li[i:]
            # 슬라이싱 할 때마다 슬라이싱된 리스트가 생성되며
            # O(k)의 시간이 소요되기 때문에(k는 슬라이스 크기)
            # 비효율적
            i = len(li) // 2
        elif num < li[i]:
            li = li[:i+1]
            i = (len(li) - 1) // 2
        else:
            return "1"
    return "1" if li[i] == num else "0"

input()
a = list(set(map(int, input().split())))
a.sort() # O(n log n)의 시간 소요

input()
b = list(map(int, input().split()))

ans = ""
for num in b:
    ans += dichotomy(a, num) + " "
print(ans[:-1])