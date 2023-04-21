a = [1]
for i in a:
    a.append(len(a) + i)
    print("hi")
    a.remove(i)

a = 1
for i in range(a):
    a += 1
    print("hi")
# for문 도중에는 range(a)가 안 늘어남

# a = [1, 2, 3]
# print(type(len(a)))


# for i in range(1, 21, 1):
#     print(i) # 1, 3, 5, 7, 9, ... 19 출력. 2는 간격
for i in range(1): # = range(0 : 1)
    print(i)
print('----------')
for i in range(1, 5):
    print(i)

# range() 괄호 내에 숫자가 하나면 0부터, 그 외에는 앞숫자부터 시작하니 주의.