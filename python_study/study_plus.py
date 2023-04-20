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

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
a = {
    "A" : {"a" : 11 , "b" : 12, "c" : 13},
    "B" : {"a" : 21 , "b" : 22, "c" : 23},
    "C" : {"a" : 31 , "b" : 32, "c" : 33}
}
print(a["A"].get("a")) # 2중 딕셔너리에서 get 쓰는법 # 11 출력

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