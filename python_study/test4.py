# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i, j, k in a:
#     print(i, j, k)

# a = [1, 2, 3, 4, 5, 6 ,7]
# a.append(a.pop(0))
# print(a)

# a = {'a1' : [1, 2, 3], 'a2' : [4, 5, 6], 'a3' : [7, 8, 9]}
# for i in a['a1']:
#     print(i)
# a = '가나다'
# print(a.startswith('가')) # True

# a = '가나다'
# print(a.contains('나'))

# a = ['가나다', '가다라', '라마바']
# print(a.startswith('가')) # 에러

# a = [1, 2, 3, 4, 5]
# print(5 in a) # True

# a = 'Hello'
# print('e' in a) # True


# def solution(n): # 피자를 7조각으로 나눌 때 n명이서 인당 최소 1개씩 먹도록 피자수 구하기
#     return (n - 1) // 7 + 1
# print(solution(10))

# def solution(dot): # (x, y) 좌표를 받고 몇사분면인지 파악하는 함수.
#     a = [(2, 1), (3, 4)]
#     return a[dot[1] < 0][dot[0] > 0] # 인덱싱을 bool을 통해 0과 1로 나눠서 함.

# if not False and True: # not은 뒤에 and 양쪽조건 둘 다 적용
#     print('hi')
# else:
#     print('bye')

# def solution(babbling):
#     a = []
#     b = ['aya', 'ye', 'woo', 'ma']
#     for i in range(4):
#         a.append(b[i])    
#         for j in range(4):
#             if j == i:
#                 continue
#             a.append(b[i] + b[j])
#             for k in range(4):
#                 if k == i or k == j:
#                     continue
#                 a.append(b[i] + b[j] + b[k])
#                 a.append(b[i] + b[j] + b[k] + b[6 - i - j -k])
#     return sum(babbling.count(i) for i in a)

# print(solution(['aya', 'yee', 'u', 'maa', 'wyeoo']))

# a = [0, 1, 2, 3]
# b = 1
# c = 3
# e = 2
# print(a[6-b-c-e])

# for i in range(1):
#     continue
#     print('hi')
# a = {1, 2, 3}
# b = {3, 4, 5, 6}
# print(min(b))

# def solution(a, b, c, d):
#     n = {a, b, c, d}
#     if len(n) == 1:
#         return 1111 * a
#     if len(n) == 2:
#         return ((max(n) + min(n)) * (max(n) - min(n)))
#     if len(n) == 4:
#         return min(n)
#     n = sorted([a, b, c, d])
#     if n.count(n[1]) == 3:
#         return n[0] and n[-1]
#     n = [i for i in n if n.count(i) == 1]
#     return n[0] * n[1]

# print(solution(2, 2, 3, 4))


# a = [1, 2, 3] # 오류
# b = [3, 4, 5]
# print(a & b)

# def solution(my_string, queries):
#     answer = ''.join(my_string)
#     for s, e in queries:
#         answer[s:e+1] = answer[s:e+1:-1]
#     return ''.join()
# solution('hello', [[2, 3], [4, 5]])

# a = ['0123456']
# b = ''.join(a)
# print(b)
# print(type(b))
# c = list(''.join(b))
# print(c)
# print(type(c))

# print(c[:6])
# print(c[6::-1])

# print([1, 2, 3, 4].count(4))

# a = [1, 2, 3]
# print('0' * (len(a) + 1))

# b = [('0' * (len(a) + 1)).split()]
# print(b)
# b = list('0000')
# print(b)

a = {1, 2, 3}
for i in a:
    print(i)