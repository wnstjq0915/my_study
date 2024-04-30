import math

def dichotomy(li, num):
    len_li = len(li) - 1
    add_i = len_li
    i = add_i

    if num < li[0] or num > li[add_i]:
        return "0"

    print(li)
    print(num)
    while add_i != 0:
        if i < 0 or i > len_li:
            return "0"
        # add_i //= 2 # 올림으로 바꾸기
        add_i = math.ceil(add_i/2)
        print(i, add_i)
        if num > li[i]:
            # 슬라이싱 할 때마다 슬라이싱된 리스트가 생성되며
            # O(k)의 시간이 소요되기 때문에(k는 슬라이스 크기)
            # 비효율적
            i -= add_i
        elif num < li[i]:
            i += add_i
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