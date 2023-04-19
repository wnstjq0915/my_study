# 조건문
# """"
# if 조건:
# (탭 한칸 or 스페이스 네칸) 실행하려는 코드
# """"
# bool값은 Ture, False로 나뉨 (예약어라 앞글자 대문자)


a = 5
if a > 3: # if문은 조건이 True일때만 안쪽 코드블럭을 실행
    print('a는 3보다 크다') # 파이썬은 들여쓰기로 코드블럭을 구분한다.
else: # if가 있어야만 사용가능.
    print('a는 3보다 크지 않다') # if가 False일때 실행

if True:
    print('무조건 실행')

if False:
    print('실행되지 않음')

a = 5
if a > 5:
    print('a는 5보다 크다')
elif a == 5:
    print('a는 5다')
else:
    print('a는 5보다 작다')


number1 = 10
number2 = 5
if number1 > number2:
    print(number1 > number2)
    print('number1이 더 크다.')
elif number1 == number2:
    print(number1 == number2) # = 한개는 같다가 아니라 대입연산자인거 조심
    print('number1과 number2는 같다')
elif number1 < number2:
    print(number1 < number2)
    print('number1은 number2보다 작다')
else:
    print('number1과 number2는 비교할 수 없다') # 숫자형과 문자형은 비교할 경우 에러가 나기에 이 코드는 실행X


print(bool(3 > 2.1)) # int 와 float은 비교 가능

# 비교 연산자
# a > b    a가 b보다 크다
# a >= b   a가 b보다 크거나 같다
# a < b    a가 b보다 작다
# a <= b   a가 b보다 작거나 같다
# a == b   a와 b는 같다
# a != b   a와 b는 같지 않다 or 다르다


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(2 > 3)  # False
print(2 >= 3) # False
print(2 < 3)  # True
print(2 <= 3) # True
print(2 == 3) # False
print(2 != 3) # True


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(bool("a" < "b")) # True, abcd 사전순(순서가 뒤에 있으면 큼)
print(bool("c" < "b")) # False
print(bool("CAT" < "DOG")) # True, 첫번째 알파벳 비교
print(bool("COW" > "CAT")) # True, 첫번째 같으니 두번째로 비교
print(bool("DOG" < "dog")) # True, 대문자 -> 소문자, 문자열끼리 비교는 == 외에 잘 안 씀

a = 0
b = '0'
print(a == b) # False, ==는 에러는 안 남


# 논리 연산자 (or bool 연산자)
# and     : a and b 일 때 둘 다 True일때만 True
# or      : a or b 일 때 둘 중 하나만 True면 True
# not     : not a 일때 a가 True면 False로, False면 True로


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(True and True)   # Ture  다 순서 상관 X
print(True and False)  # False
print(False and False) # False
print(True or True)    # Ture
print(True or False)   # Ture
print(False or False)  # False
print(not True)        # False  not은 항이 하나이기 때문에 단항 연산자
print(not False)       # Ture


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
age = 23
money = 10000

if age >= 20 and money >= 10000:
    print("성인이고 부자입니다.")
elif age < 20 and money >= 10000:
    print("학생이고 부자입니다.")
elif age >= 20 or money >= 10000:
    print("성인 또는 부자입니다.")


print('ㅡㅡㅡㅡㅡㅡㅡㅡ')
if "안녕": # 문자형은 값이 있으면 Ture, 없으면 False
    print("안녕하세요")

if 0: # 숫자형은 0이면 False, 0이 아니면 True
    print(0)

print(bool(2)) # 트루


