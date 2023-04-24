# function함수
# 입력 - > 처리 -> 출력
# input을 받아서 ( 입력 )
# 특정 작업을 수행하고 ( 처리 )
# output을 반환한다 ( 출력 )

# 내장 함수(builit-in)
# 파이썬이 기본적으로 제공해주는 함수
# print(), len(), zip(), int(), list(), range 등

# abs(값)
# absolute의 약자
# 입력한 숫자형 데이터의 절댓값을
# 반환한다.

print(abs(100)) # 100 출력
print(abs(-100)) # 절대값이 반환되어 100 출력
print(abs(-3.14)) # 실수형도 가능


# sum(리스트)
# 리스트 안의 숫자를 모두 더한다.
# 더한 값을 반환한다.

a = [1, 2, 3, 4]
print(sum(a)) # 10 출력
sum([1, 2, 3, 4, 5]) # 15 출력


# max(리스트)
# 리스트 안의 최댓값을 찾아 반환한다.
print(max([1, 2, 3, 4, 5])) # 5 출력

# min(리스트)
# 리스트 안의 최솟값을 찾아 반환한다.
print(min([1, 2, 3, 4, 5])) # 1 출력

# li_1 = [1, 2, 3]
# min(li_1)
# li_1.append(4)
# 여기서 append는 리스트의 함수이고, min은 내장함수
# 리스트에 종속되는 함수가 아닌 것에 주의

# chr()
# 정수를 입력받고
# 정수 1개를 입력받고 해당하는
# 유니코드 문자를 반환한다.
print(chr(65)) # A 출력

# ord()
# 문자를 1개 입력받고 해당하는
# 정수를 반환한다.
print(ord('A')) # 65 출력


# round(값)
# rount(값, 소수 자릿수)
# 반올림 함수
print(round(1.234)) # 1
print(round(1.369, 1)) # 1.4
print(round(1.234, 2)) # 1.23
print(round(314, -2)) # 300



# 함수 정의(define)
# 함수 이름
# 함수 입력값 parameter
# 함수 결과값 return value
"""
def 함수이름(함수입력값):
    함수기능코드
    return 함수 결과값
"""
# def는 함수를 정의하는 명령어
# 함수이름도 변수 이름처럼
# 규칙을 지켜서 지어야 한다.
# 영어, 숫자, _만 사용
# 숫자로 시작하면 안됨
# 띄어쓰기하면 안됨
# 키워드 사용하면 안됨(if, for, print 같은 이름 X)
# 이미 있는 내장함수를 이름으로 사용했을 때(ex: print())
# 내장함수가 내가 만든 함수로 덮어씌워짐.
# 이름을 봤을 때 무슨 기능을 할지 예측 가능하게
# 잘 짓는게 중요

def print_names(): # 입력값이 없는 함수
    print("손흥민")
    print("황희찬")
    print("김민재")
    print("이강인")
# return이 없는 출력값이 없는 함수

print_names() # 함수 불러오기


def get_name():
    return "이름"

def print_my_name():
    print(get_name())

print_my_name() # 이름 출력


a = print(10) # a 변수에 프린트를 못 담음
b = range(10) # b 변수에 0부터 9까지의 값을 담음

print("------------------------")
a = print_my_name() # 리턴이 없음
b = get_name() # 리턴이 있음
print(a) # None. 리턴값이 없기에.
print(b)


# parameter
# 함수에 입력하는 값
# 매개변수, argument 혼용
def add(a, b):
    return a + b

def print_add(a, b):
    print(a + b)
# 순서대로 a와 b에 입력받음

print(add(4, 7))
print(print_add(3, 6)) # 9 호출 후 none

add(2, 3) # 이것만 쓰면 print 정의가 없기에 출력X
# 임시적으로 선언하고 할당하는 느낌
result = (add(1, 2)) # result에 3 할당

result = print_add(1, 2) # 함수가 실행돼서 3 출력 후 result에 3 할당
# 매우매우 중요.

print(result) # 리턴이 없는 함수를 result에 할당했기에 none값 출력

# add값을 출력하고 싶다면
print_add(1, 2)
print(add(1, 2))
# 둘 중 하나


print_add("안녕", "하세요") # 에러가 안 남.
# add함수를 실행시켜, "안녕" + "하세요" 실행.
# 만약 숫자와 문자열을 섞을 경우 에러

print_add(b = "하세요", a = "안녕")
# 순서를 지정해서 넣을 수 있음.


def swap_number(a, b):
    temp = a
    a = b
    b = temp
    print(a, b)

# a랑 b를 바꾸는 함수
swap_number(1, 2)
print("------------------")
a = 1
b = 2
print(a, b)
swap_number(a, b) # 함수에 1,2 넣어서 2, 1 출력
print(a, b) # 함수호출 후 1, 2 출력
# 파이썬도 지역변수 적용
# 전역변수 a = 1, b = 2와는 별개로 함수 내에서만 사용됨.
# if문, for문 또한 같음.

a = 1
b = 2

def swap_number(a, b):
    temp = a
    a = b
    b = temp
    print(a, b)
    return a, b # return값에 넣는 변수는 전역변수

print("--------------------")
a, b = swap_number(a, b)
print(a, b) # 2, 1 정상적으로 바뀜
# 파이썬은 변수 갯수와 값 갯수가 같으면 동시에 할당 가능
a, b, c = 1, 2, 3
print(a, b, c) # 1, 2, 3
d, e, f= [4, 5, 6] # 리스트랑 튜블도 똑같이 가능, 인트로 가져옴.

temp = a
a = b
b = temp
# 한줄로 요약 가능
a, b = b, a # 정상적으로 잘 바뀜

"""
함수를 정의하세요.
함수 이름 : mul
함수 입력값 : 정수 2개
함수 출력값 : 정수 2개의 곱
"""

def mul(a, b):
    return a * b

print(mul(4, 5)) # 20 잘 나오는지 확인


# 기본값 매개변수
# default value parameter
# 함수 호출 시 n2에 입력된 값이 없으면
# 기본값 사용
def mul(n1, n2 = 3):
    return n1 * n2

print(mul(7)) # 7과 기본값 3이 곱해지며 21 출력


# def test_func(x, test[]): # 에러
#     print(x, test)
# test_func(1, [1, 2, 3])

# 리스트는 값이 누적됨. 빈 리스트가 다시 생성되는 것이 아닌, 계속 쓰임.
# 리스트를 기본값으로 사용하지 말것.

def test_func1(x, test = 5):
    test = test
    print(x, test)

test_func1(1)
test_func1(2)


def test_func2(x, test = None):
    if test == None:
        test = []
    test.append(x)
    print(x, test)


# def sub(n1, n2 = 0, n3):
#     print(n1 - n2 - n3) # Error. 기본값이 설정된 매개변수는 기본값이
# 없는 매개변수 뒤로 가야됨.


# 1 ~ 10까지 더하고 싶을 때
# *를 사용한 매개변수
# 입력값이 몇개가 될지 모를 때(안 정해졌을 때)
def add_many(*args):
    # 튜플처럼 사용
    # 인덱싱, 슬라이싱 가능.
    result = 0
    for i in args:
        result += i
    return result

print(add_many(7, 8))
print(add_many(4, 7, 8))


def calc_many(n1, *args): # 일반 매개변수랑도 사용가능
    result = n1
    for i in args:
        result += i
    return n1
# def calc_many(*args, n1): 매개변수 순서 바꿔서도 가능


# 키워드 매개변수
# **kwargs. 관용적 표현
# keyword argument의 줄임
# 딕셔너리로 사용
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1, b = 2)
print_kwargs(name = '이름', age = 10)


# 함수의 반환
# return 반환값
# return을 만나면 반환값을 반환함과 동시에
# 함수가 종료된다.

def test_function_5():
    print(1)
    print(2)
    return None
    print(3)
    print(4)
    print(5)
# 함수의 반환값은 무조건 1개이다.
def test_func_6(a, b):
    return a + b, a * b
#     return (a + b, a * b) 와 같음. 결과값은 투플형태로 나옴.
print(test_func_6(1, 2))

result = test_func_6(1, 2)
res_add, res_mul = test_func_6(1, 2)
# res_add, res_mul = test_func_6(a+b, a*b)
print(result)
print(res_add, res_mul)

"""
홀수 판별 함수
정수 1개를 입력받고 홀수인지
판별하는 함수
함수 이름: is_odd_number
파라미터: n
반환값: 홀수면 True
        짝수면 False
"""

def is_odd_number(n):
    if abs(n) % 2 == 1:
        return True # 리턴값은 반환과 동시에 함수를 중단하기 때문에
    return False # else가 없어도 됨.

# 최적의 답
def is_odd_number(n):
    return abs(n) % 2 == 1 # 어차피 True랑 False값만 보기에
# 논리연산자만 써서 bool형으로 출력해도 가능.

# print(is_odd_number(int(input("정수: "))))


"""
테두리를 출력하는 함수
문자열을 입력받고 print
함수를 이용해 테두리와 함께 문자를 출력한다.
함수이름: get_borderd_str
파라미터: message
반환값: None
print 예시:

*****
hello
*****

(*은 문자열 길이만큼)
""" # 출력과 반환값을 헷갈리면 안 됨!

def get_borderd_str(message):
    print(f"""{"*" * len(str(message))}
{message}
{"*" * len(str(message))}""") # 숫자형에도 len을 쓰기 위해 str 넣기 iterable값만 가능

# get_borderd_str(input("메세지: "))

get_borderd_str(12345)


"""
속도를 변환하는 함수
m/s단위의 속도가 입력되면
km/h단위의 속도로 변환한다.
함수 이름: convert_velocity
파라미터: velocity
반환값: km/h로 변환된 속도
"""
# 나누기 1000, 곱하기 3600
# = 3.6

def convert_velocity(velocity):
    return velocity * 3.6
print(convert_velocity(4))


"""
*
**
***
****
n = 4일때
모양 찍기

별 찍기 함수
정수를 함수에 입력하여
호출하면 해당 정수 줄의
별을 화면에 출력한다.
함수이름: print_stars
파라미터: n
반환값: None
"""

def print_stars(n):
    for i in range(1, n + 1):
        print("*" * i)
print_stars(7)


# 2중 for문
def print_stars(n):
    for i in range(n):
        for j in range(i+1): # j를 쓰지 않았으며 print 또한 변수가 들어가있지 않으므로 반복횟수가 중요.
            print("*", end="") # print는 end가 기본으로 들어가 있으나, end = ""해서 줄바꿈을 안 함.
        print() # 아무것도 출력 안 하고 end 기본값인 줄바꿈만 출력


# while문
def print_stars(n):
    i = 0
    while i < n:
        j = 0
        while j < i + 1:
            print("*", end = "")
            j += 1
        print()
        i += 1


"""
가운데 별도 해보기
"""

def print_stars(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" + "**" * (i) + " " * (n - i - 1))
# print_stars(int(input("정수: ")))

## print("*" + "**" * (i)) # 별의 개수