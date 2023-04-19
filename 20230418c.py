# 파이썬은 다른 컴파일러를 쓰는 다른 언어와는 다르게 인터프리터를 쓰는데
# 인터프리터는 한번에 변환하는 컴파일러와는 다르게
# 한줄씩 변환과 출력을 반복하기 때문에 컴파일러보다 약간 느림


print('안녕하세요.'+'반갑습니다.')
print('안녕하세요'*5)


# print('안녕하세요'+10) Error 문자열 + 숫자


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ') # 인덱싱
print('hello'[0])
print('hello'[1])
print('hello'[2])
print('hello'[3])
print('hello'[4])


# print('hello'[4]*5) 도 가능


print('ㅡㅡㅡㅡㅡㅡㅡㅡ')
print('abcde'[-1]) # e
print('abcde'[-2]) # d
print('abcde'[-3]) # c
print('abcde'[-4]) # b
print('abcde'[-5]) # a
print('hello'[1:3]) # 1~2번 인덱스 출력 (인덱스 위치 생각하면 쉬움)(화살표로 생각)


#인덱스0은 첫번째 문자 바로 전 지점, 인덱스 1은 두번째문자 바로 전 지점.
# 그렇기에 [1:3]은 el만 출력


print('ㅡㅡㅡㅡㅡㅡㅡㅡ') # 슬라이싱
print('hello'[:3]) # hel
print('hello'[2:]) # llo
print(len('hello')) # len 은 길이확인 가능(데이터의 길이 체크)


# print('hello'[100]) # error out of index 범위초과
# [-100]도 안됨


# 함수
# 특정 동작을 수행하는 코드의 집합
# 합수를 정의(definition)
# 함수를 호출(call)
# x라는 변수를 받아 f(x)라는 함수의 공정을 거친 후 y의 리턴값을 반환받음
# ex) len('hello') 는 hello라는 입력을 받아 len이라는 함수를 거쳐 5라는 리턴값을 반환받음



a = 'abcdefghijk' # 추가로 메모
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

number = 10
day = "three"
a = "I ate %s apples. so I was sick for %s days." % (number, day)
print(a)


i = 'Jhon' # i가 a보다 늦게 선언될 경우 에러남.
a = "hello %s" % (i)
print(a)

# %s 문자열 (웬만한거 다 됨) (숫자도 문자로 바껴서 들어감)
# %c 문자 1개
# %d 정수
# %f 부동소수
# %o 8진수
# %x 16진수
# %% Literal % (문자 '%' 자체)
