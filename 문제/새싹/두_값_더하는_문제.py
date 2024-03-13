"""
입력예시:
2 3
"""
print((lambda x,y: x+y)(*map(int, input().split())))

"""
설명
map을 통해 [숫자1, 숫자2]의 값을 반환한 뒤에
*를 통해 개별값을 lambda에 전달하여
두 수 더하여 프린트
"""

# 정석
# a, b = map(int, input().split())
# print(a + b)

# 다른 사람 숏코딩
# print(sum(*open(0,"rb"))%23)
# ???