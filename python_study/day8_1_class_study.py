# # 객체지향(oop, object oriented programming)
# # 객체와 객체 사이의 상호작용으로 프로그램을
# # 구성하는 프로그래밍 패러다임

# # 객체지향의 특징
# # 추상화: 공통된 속성이나 기능 도출
# # 캡슐화: 데이터의 구조와 연산을 결합
# # 상속: 상위 개념의 특징이 하위 개념에 전달
# # 다형성: 유사 객체의 사용성을 그대로 유지


# # 객체는 추상화와 캡슐화의 결과
# # 객체는 데이터 필드와 메소드를 가진다.

# # 클래스는 객체를 정의한 것(객체의 설계도)
# # 데이터 필드(멤버 변수, 속성)
# # 객체가 가지고 있는 변수

# # 메소드
# # 객체가 가지고 있는 함수


# """
# class 클래스이름:
#     클래스 멤버 변수
#     메소드
# """
# # 클래스 이름도 변수 이름 규칙 지켜야 함
# # 클래스 이름 컨벤션(관용)
# # 첫글자 대문자
# # 언더바(_) 안쓰기
# # 단어 구분될 때 대문자

# class Car:
#     def move(self): # 클래스 내부에 있는 함수를 메소드.
#         print("move")
# class SportsCar:
#     pass

# # 인스턴스
# # 객체
# # 클래스를 통해 생성된 객체
# my_car = Car() # class를 호출하면 class객체가 생성됨. 객체가 my_car변수에 할당됨.
# my_car.move() # my_car는 Car 클래스의 인스턴스(객체)다 이런식으로 말함
# # . 은 객체 멤버 접근 연산자
# # 리스트도 객체였음

# li = [1, 2, 3, 4, 5]
# li.append(6) # .을 써서 append를 사용

# # 파이썬에서는 모든게 객체
# # 내장함수 type
# # 데이터의 자료형을 반환
# print(type(li)) # class 'list'라고 출력. list형 객체
# n = 10
# print(type(n)) # class 'int', 정수형 객체
# print(type("Hello")) # class 'str'

# # str(문자열) 메소드
# # 원본은 수정되지 않고 새로운 값을 만듦.

# # upper()
# # 모두 대문자로 변경
# s = "Hello"

# print(s.upper()) # Hello.upper()과 같이 변수선언 없이 바로 써도 됨.

# # lower()
# # 모두 소문자로 변경
# print(s.lower())

# # strip()
# # 문자열 양쪽 끝의 특정 문자를 제거
# s1 = "   Hello   "
# print(s1.strip()) # 공백 제거되고 Hello 출력
# # lstrip(), rstrip()
# # 왼쪽, 오른쪽 끝의 특정문자 제거

# # split()
# # 구분자로 분할하여 리스트로 반환
# s2 = "Hello, world, Python"
# print(s2.split(', '))

# # replace()
# # 문자열의 특정 부분을 대체
# print(s2.replace(', ', '|')) # ', '를 '|'로 바꿈

# s2 = s2.replace(',', ' |') # 수정이 아닌 재할당
# print(s2)

# # "Hello" --> "hello"
# s3 = "Hello"
# # s3[0] = "h"
# # print(s3) # 에러가 남. 스트링은 수정이 안 되는 immutable값이라서.
# # 재할당하는 것은 가능함.

# # lower나 replace 같은 메소드를 사용한다면 수정이 아닌 재할당.
# s3 = s3.lower()
# print(s3)


# self 매개변수
# 모든 메소드의 첫번째 매개변수
# 메소드의 정의에는 사용되지만, 호출에는
# 사용되지 않음
# 객체 자신을 참조하여 클래스에 정의된
# 멤버에 접근할 때 사용

# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# class person:
#     def say(self): # 클래스 안에 정의된 메소드들의 첫번째 매개변수는 self 고정
#         self.name = "사람1" # 다른 메소드에서도 사용가능
#         print("Hello")
#     def move(self):
#         pass
#     def eat(self, food):
#         self.sleep() # 메소드 안에서도 다른 메소드 사용가능
#         print(f"{self.name}이 {food}를 먹었습니다.")
#     def sleep(self):
#         print(f"{self.name}이 잠을 잤습니다.")

# person1 = person()
# person1.say()
# person1.eat("밥")

# initializer
# 초기자
# initialize 초기화. initial -> 시작. 비운다X, 값을 가지게 만든다
# class Person:
#     def __init__(self, name, age, gender, phone): # 특수메소드. 클래스 선언되면 바로 실행됨
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.phone = phone # 초기화 할 때 이렇게 입력받는게 정석
#         print("initialize")
#     def say_name(self):
#         print(self.name) 
#     def introduce(self):
#             print(self.name)
#             print(self.age)
#             print(self.gender)

# print("before")
# person2 = Person("이름", 20, "남자", "010-1234-5678") # class 호출과 동시에 작동
# print("after")
# person2.say_name()


"""
Person 클래스에 introduce 메소드를 추가
이름, 나이, 성별을 print하는 메소드
""" # 추가완료
# 단축키
# 쉬프트 + 알트 + 화살표(위 or 아래) = 현재 줄을 위 또는 아래로 복붙


# 상속 inheritance
class Animal:
    def __init__(self, name):
        self.name = name # 멤버변수로 저장 # 값이 똑같은 다른 객체
        print(f"{self.name}이(가) 생성되었습니다.")
        self.say()

    def say(self):
        print("")

class Dog(Animal): # Animal이 Dog의 부모클래스가 됨
    def say(self): # 메소드 재정의, method overriding. 이미 부모클래스에 있는 say메소드를 덮어씌움
        print("멍멍")

my_dog = Dog("백구")

class Cat(Animal):
    def say(self):
        print("야옹")

my_cat = Cat("고양")


class Student:
    def __init__(self, name, age, school, grade):
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade

    def introduce(self):
        print(f"이름: {self.name}")
        print(f"나이: {self.age}")
        print(f"학교: {self.school}")
        print(f"학년: {self.grade}")

stu1 = Student("홍길동", 20, "서울대학교", 1)
stu2 = Student("손흥민", 21, "서울대학교", 2)
stu3 = Student("류현진", 22, "서울대학교", 3)
stu_list = [stu1, stu2, stu3]
for stu in stu_list:
    stu.introduce() # 한명씩 introduce