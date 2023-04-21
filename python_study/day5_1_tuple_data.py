# tuple 튜플형
# 튜플은 element값을 수정할 수 없다.

# mutable / immutable 변하는 / 변하지 않는
# mutable
# list, dictionary
# immutable
# int, float, str, tuple

my_list = [1, 2, 3]
print(my_list)
my_list[0] = 5
print(my_list) # [5, 2, 3]

my_tuple = (1, 2, 3)
print(my_tuple) # (1, 2, 3)
# my_tuple[0] = 5 # Error. 튜플형은 수정 불가능
# print(my_tuple) # 실행 X

# 리스트가 가능한거 웬만해서 다 가능
tuple_1 = ("Hello", "world", "python")
t2 = (1, 2, 3, 4, 5)
t3 = (1, 2, "Hello")
t4 = 1, 2, 3 # 괄호 생략도 가능. 그러나 가독성을 위해 괄호 쓰는게 좋음.
t5 = (1, 2, (3, 4, 5)) # 리스트와 마찬가지로 튜플 안에 리스트나 딕셔너리도 넣을 수 있음

t6 = tuple_1 + t2 # 가능
t7 = t3 * 3 # 가능
print(t7) # t3이 세번 출력됨
t7 = t3 * 4
print(t7) # t3이 네번 출력됨
t2 = 3, 4, 5
print(t2)
# t7이나 t2나 수정이 아니라 할당이 세로 된거라 에러 안 남.


t3 = (1, 2, "hello")
# 인덱싱이랑 슬라이싱 가능
print(t3[2]) # "hello" 출력
print(t3[:2]) # 1, 2 출력
# 슬라이싱은 타입을 안 바꾸고 가져옴. 그렇기에 위에 1과 2는 튜플형태로 가져옴.

print(type(t3[2])) # hello, str
print(type(t3[:2])) # tuple

print(len(t3)) # 3 출력. len도 가능

t5 = (1, 2, (3, 4, 5))
print(t5[2][1]) # 4 꺼내짐

t8 = (5, 3, 1, 4, 2)
# 정렬을 하고 싶으나 정령은 값이 바뀌는 것이기에 에러.

# 튜블도 이터러블값이라 for문 가능
for i in t8:
    print(i) # 5, 3, 1, 4, 2 하나씩 5번 출력. i가 왜 1~5 순서로 할당되는 것이 아닌지 알아야 함.