# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i, j, k in a:
#     print(i, j, k)

# a = [1, 2, 3, 4, 5, 6 ,7]
# a.append(a.pop(0))
# print(a)

a = {'a1' : [1, 2, 3], 'a2' : [4, 5, 6], 'a3' : [7, 8, 9]}
for i in a['a1']:
    print(i)
# a = '가나다'
# print(a.startswith('가')) # True

# a = '가나다'
# print(a.contains('나'))

# a = ['가나다', '가다라', '라마바']
# print(a.startswith('가')) # 에러

a = [1, 2, 3, 4, 5]
print(5 in a) # True

a = 'Hello'
print('e' in a) # True
