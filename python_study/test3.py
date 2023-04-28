# print_add(3, 5)

# def add(a, b):
#     return a + b

# def print_add(a, b):
#     print(a + b)

# 파이썬은 함수 호이스팅 불가능.
# print(a) 에러뜸. 파이썬도 지역변수개념 적용

# a = 1
# if a == 1:
#     b = 2
# print(b)
# # if는 지역변수?, 전역변수?

# a = 1
# b = 2
# a, b = b, a
# print(a, b)

# def test_func(x, test[]): # 에러
#     print(x, test)
# test_func(1, [1, 2, 3])

# for i in range(3, 0): # 앞의 값이 더 크더라도 에러는 나지 않음. 실행은 안 됨.
#     print(i)

# i = int(input("정수: "))
# if i % 3 or i % 5 == 0: # i % 5 == 0 만 적용됨.
#     print(f"{i} = 3의 배수거나 5의 배수")

# a = [1, 2, 3, 4, 5]
# print(len(a)) # 리스트 길이 5 출력

# a = []
# a.sort() # 리스트가 비어도 sort는 에러없이 작동.
# print(min(a)) # 리스트 안에 값이 없으면 min은 에러

# a = [1, 2, 3, 4, 5]
# print(5 - a.pop(0)) # 리스트에서 바로 빼서 사용 가능
# print(a)

# def test():
#     print("test")
# a = test() # 함수 호출과 동시에 작동. a에 할당과 동시에 프린트됨.
# print(a)

# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # overriding 했을 때 덮어 씌우는지 추가하는지 테스트
# class Test1:
#     def print_test(self):
#         print("overriding 테스트")

# class_test1 = Test1()
# class_test1.print_test()
# # 재정의 테스트 출력

# class Test2(Test1):
#     def print_test(self):
#         print("overriding 테스트2")

# class_test2 = Test2()
# class_test2.print_test()
# # 결과: 완전 새로 덮어씌움

# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ') # * arge 판정
# def calc_many(n1, *args): # 일반 매개변수랑도 사용가능
#     result = n1
#     for i in args:
#         result -= i
#     return result
# print(calc_many(100, 3, 4, 5))

# def calc_many(*args, n1):
#     result = n1
#     for i in args:
#         result -= i
#     return result
# # 밑에 프린트 다 에러남.
# # print(calc_many(3, 4, 5, 100))
# # print(calc_many(n1 = 100, 3, 4, 5))
# # print(calc_many(n1 = 100, args = 3, 4, 5))

# # 결과: *args 같은 경우에는 일반 매개변수 뒤에 받도록.

# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# a = range(1, 10)
# print(a)

# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ') # find랑 cound
# a = ["1", "2", "3"]
# b = "123456"
# print(a.count("1"))
# print(b.find("3"))
# # find는 문자열만 되고, find는 인덱스, count는 갯수를 출력함
# print(b.index("4")) # 4의 인덱스인 3 출력

# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# a = "123  "
# print(a.isdigit())


# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# s1 = "   Hello   "
# print(s1.strip()) # 공백 제거되고 Hello 출력
# # lstrip(), rstrip()
# # 왼쪽, 오른쪽 끝의 특정문자 제거

# import datetime
# # 며칠동안 수강하는지
# day1 = datetime.date(2023, 4, 17)
# day_end = datetime.date(2023, 9, 18)
# diff = day_end - day1
# print(diff.days)

# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # 슬라이싱 범위 헷갈려서
# a = "abcde"
# print(a[:3])

# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ') # for문도 break continue 먹힘
# for i in range(4):
#     print(i)
#     continue
#     print(i)


from bs4 import BeautifulSoup
html = "<html><body>Hello</body></html>"
soup = BeautifulSoup(html, "html.parser")
print(html) # 내용은
print(soup) # 둘 다 같음

print(soup.body.text) # html은 soup와 같이 .body.text 같은거 못 붙임
print(type(soup.body.text))