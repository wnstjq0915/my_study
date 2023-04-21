name = "John"
print(f"my name is {name}")

a = "hello"
print(a[0])

li_1 = ["Hello", "World", "Python"]
li_2 = [1, 2, 3]

a = li_1.insert(1, li_2[0]) # insert는 pop처럼은 안 됨
print(a)
print(li_1)
print(li_1.pop(1))

print(323.0 + 60)

print("True" == True) # 문자열과 숫자열 같지 않다 뜸
a = 1
print("hello" + str(a)) # str() 스트링 값으로 변환, int()와 같은 판정


a = 31
a //= 2 # //= 가능
print(a)


# 2중 딕셔너리 테스트
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
a = {
    "A" : {"a" : 1 , "b" : 2, "c" : 3},
    "B" : {"a" : 1 , "b" : 2, "c" : 3},
    "B" : {"a" : 1 , "b" : 2, "c" : 3}
}
print(a["A"].get("a")) # 2중 딕셔너리에서 get 쓰는법

a = 2
print(type(a))
print(str(a))
a = str(a) # print(str(a)) 는 프린트 내에서만 바뀜
print(type(a))
print(type(a))