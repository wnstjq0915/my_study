# &는 비트연산자.
3 & 4 == 0
# 3은 0011
# 4는 0100
# 같은 자릿수가 1일때만 1이 돼서 0000값으로 바뀜.
3 and 4
# 4값 반환. 받은값 중 높은값 반환
3 or 4
# 3 반환. or 은 낮은값 반환

a = 'abcdefghijk'
print(a[0:10:2]) # 인덱스 0부터 10까지 2의 간격으로 출력. 결과 acegi
print(a[::2]) # acegik
print(a[::-2]) # kigeca

print('ㅡㅡㅡㅡㅡㅡㅡㅡ') # 이런게 있다 정도만
a = "{name}은 {age}이다.".format(age = '17살', name = "철수") # 순서 상관없이 대입가능
print(a)

a = "안녕 {}.".format("민수")
print(a)

print('ㅡㅡㅡㅡㅡㅡㅡㅡ')
a = "My favorite number is %d." % 3 # %d에 3이 들어감. 숫자만 가능, % 뒤에 씌어쓰기 주의
print(a) # My favorite number is 3. 출력. 이런 방식은 수정이 편함.

a = "My favorite number is %10d." % 3 # 거의 안 쓰이지만 알아만 두기
print(a) # 3 앞에 10칸의 공백이 생김

number = 10
day = "three"
a = "I ate %s apples. so I was sick for %s days." % (number, day)
print(a)

i = 'John' # i가 a보다 늦게 선언될 경우 에러남.
a = "hello %s" % (i)
print(a)

name = "John"
print(f"my name is {name}") # " 앞에 f를 붙일 경우 문자열 내에 변수 추가 가능, f는 format인듯

a = "%0.4f" % 3.141592 # "%간격.소수점 남기는 자리 수f"
print(a) # 반올림돼서 3.1416으로 나옴

a = "hobby"
print(a.count('b')) # a 변수에서 b가 몇개 있는지 출력

a = "banana"
print(a.index('a')) # 인덱스는 주로 리스트에서만 활용(문자열도 가능하긴 함)
print(a)
print(a.find('a')) # a의 위치(인덱스)인 1 출력
print(a.find('e')) # find는 인덱스와 다르게 없으면 에러말고 -1 출력

a = ",".join("abcd") # join에 있는 값을 한 문자씩 ","를 기준으로 나눠서 a에 할당
print(a)
a = " ".join("abcd") # join에 있는 값을 한 문자씩 " "를 기준으로 나눠서 a에 할당
print(a)
a = ",".join(["a", "b", "c"]) # join은 주로 리스트에서 많이 씀
print(a) # a, b, c

a = "hi"
print(a.upper()) #"HI" 대문자로 변경
print(a) # "hi"
b = a.upper()
print(b) # "HI"
# upper <-> lower


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # 얕은복사, 깊은복사?
# 일반적인 경우
a = 1
b = 2
print(a, b)
a = b
print(a, b)
b = 3
print(a, b)
# 1 2
# 2 2
# 2 3

# 리스트의 경우
a = [1]
b = [2]
print(a, b)
a = b # a의 주소가 b의 주소로 할당. a가 b의 주소에 귀속됨.
print(a, b)
b.append(3) # b에 3을 추가
# b = [3] # 재할당은 안 됨.
print(a, b) # a는 건드리지 않았는데 b와 마찬가지로 3 추가
# 1 2
# 2 2
# 2,3 2,3
# 리스트의 경우에는 변수에 변수를 넣으면 그 주소를 복사해서 넣음.

# 값만 복사하고 싶을 경우
a = [1]
b = [2]
print(a, b)
a = b[:] # 값만 복사
print(a, b)
b.append(3)
print(a, b)
# 1 2
# 2 2
# 2 2,3

# 2차원 리스트의 경우는 좀 다름.
a = [[1, 2], [3, 4]]
b = a[:]
print(a, b)
a[0][1] = 100
print(a, b)
# a[0][1] 을 바꿨는데 b[0][1]도 바뀜

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
a = '     hi     '
print(a.strip()) # 공백을 없애줌.

a = "Life is too short"
print(a.replace("Life", "leg")) # 문자열 바꾸기. Life가 leg로

a = a.split() # 공백 기준으로 쪼개서 리스트로 a에 할당
print(a)
print(type(a))
# .split(',') 이면 , 기준으로 쪼갬.
# .split(' ', 1) 이면 ' ' 기준으로 처음 한번만 쪼개서 리스트에 넣음


# %s 문자열 (웬만한거 다 됨) (숫자도 문자로 바껴서 들어감)
# %c 문자 1개
# %d 정수
# %f 부동소수
# %o 8진수
# %x 16진수


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
a = 1
print(type(a)) # 변수타입 확인 가능
a = '1'
print(type(a)) # '' 붙이면 문자형(string)

# 연산자 우선순위 나중에 확인할 것


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
a = ["a", "b", "c"]
a[0:2] = []
print(a) # 인덱스 0에서 1까지가 없어지면서 c만 남게 됨
# del a[0:2] 도 같음

# sort의 정렬은 정수형뿐만아니라 ㄱㄴㄷ나 abc순 정렬


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # 리스트 내의 값 합치기, join함수
a = ["1", "2", "3", "4", "5"]
a = ''.join(a)
print(a) # 문자열 12345로 출력

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
a = {
    "A" : {"a" : 11 , "b" : 12, "c" : 13},
    "B" : {"a" : 21 , "b" : 22, "c" : 23},
    "C" : {"a" : 31 , "b" : 32, "c" : 33}
}
print(a["A"].get("a")) # 2중 딕셔너리에서 get 쓰는법 # 11 출력. ['A']["a"] 도 가능

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # for문 판정
a = [1]
for i in a:
    a.append(len(a) + i)
    print("hi")
    a.remove(i)
# 리스트 내의 값이 계속 변하는 길이 1개짜리 리스트를
# i에 할당했으나 한번만 실행됨.

a = 1
for i in range(a):
    a += 1
    print("hi")
# for문 도중에는 range(a)가 안 늘어남

# 그러나 리스트에 값을 계속 더해 길이를
# 계속해서 늘리는 방식은 계속해서 실행됨.

# 결론
# for문은 iterable값의 인덱스가 1씩 늘어나면서 반복됨.

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # 딕셔너리 값을 in을 통해 bool형으로 출력하기
a = {1: "일", 2: "이", 3: "삼"}
print(4 in a) # a에 4가 없기에 False 출력

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # for문에 딕셔너리 써서 값을 두개씩 넣기.
a = {1: "일", 2: "이", 3: "삼"}
for i, j in a.items():
    print("키는: " + str(i))
    print("벨류는: " + str(j))

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
"""

""문자열의 구성 파악하기""

.isalnum()
알파벳 또는 숫자 구성인지

.isalpha()
알파벳 구성인지

.isidentifier()
식별자(변수나 클래스명으로 가능한 값)로 사용할 수 있는지

.isdecimal()
정수 형태인지

.isdigit()
숫자로 인식될 수 있는지

.isspace()
공백으로만 구성되어 있는지

.islower() / isupper()
소문자 / 대문자로만 구성되어 있는지
"""

print("a1b2c3".isalnum()) # True
print("#a@b$c^#".isalnum()) # False

print("abc".isalpha()) # True
print("a1b2c3".isalpha()) # False

print("data".isidentifier()) # True
print("1_data".isidentifier()) # False, 변수명이나 클래스명은 숫자로 시작X

print("1234".isdecimal()) # True
print("0110".isdecimal()) # True
print("-111".isdecimal()) # False
print("3²".isdecimal()) # False

print("1234".isdigit()) # True
print("0110".isdigit()) # True
print("-111".isdigit()) # False
print("3²".isdigit()) # True

print(" ".isspace()) #True
print(".    ".isspace()) # False

print("abcde".islower()) # True
print("ABCDE".isupper()) # True
print("AbCdE".islower()) # False