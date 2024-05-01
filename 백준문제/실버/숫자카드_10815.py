def dichotomy(li, num):
    i = len(li) - 1

    if num < li[0] or num > li[i]:
        return "0"
    elif num == li[0] or num == li[i]:
        return "1"

    min_i, max_i = 0, i
    add_i = 1

    # 기존코드는 슬라이싱을 활용하여 리스트 자체를 반씩 자름
    # 슬라이싱 할 때마다 슬라이싱된 리스트가 생성되며
    # O(k)의 시간이 소요되기 때문에(k는 슬라이스 크기)
    # 비효율적
    while add_i != 0:
        if num > li[i]:
            min_i = i
        elif num < li[i]:
            max_i = i
        else:
            return "1"
        add_i = (max_i-min_i) // 2
        i = min_i+add_i
    return "0"

input()
a = list(set(map(int, input().split())))
a.sort() # O(n log n)의 시간 소요

input()
b = list(map(int, input().split()))

for num in b:
    print(dichotomy(a, num), end=" ")