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