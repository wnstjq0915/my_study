# 표준 라이브러리
# 파이썬에서 지원하는 표준 라이브러리
# 파이썬을 설치할 때 자동으로 함께 설치
# 따로 설치하지 않고 import 명령어로 불러옴

# datetime 라이브러리
# 날짜 관련 라이브러리
# datetime의 date 객체 사용

import datetime

# 며칠동안 수강하는지
day1 = datetime.date(2023, 4, 17)
day_end = datetime.date(2023, 9, 18)
diff = day_end - day1
print(diff.days)

# 2018년 8월 6일 무슨 요일일까요?
# weekday() -> 0 월요일, 1 화요일 ~ 6 일요일
day = datetime.date(2018, 8, 6)
weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
print(day.weekday()) # 0 출력
print(weekdays[day.weekday()]) # 월요일 출력

# datetime의 포매팅 코드
# 날짜랑 시간 표시하는 방법
# 평소 우리나라는 년/월/일 사용
# 월/일/년 같이 표기할 때도 있음

today = datetime.datetime.today()
print(today) # 2023-04-27 10:50:13 .......
# strftime()
print(today.strftime("%Y년 %m월 %d일")) # 2023년 04월 27일
# %Y 년도 4자리 다
# %y 년도 2자리
# %m 월
# %d 일
# %H 시간(24시간)
# %I 시간(12시간)
# %M 분
# %s 초
# %A 요일
print(today.strftime("%A")) # Thursday


# time 라이브러리
# 시간 관련
import time
time_now = time.time()
# print(time_now) # utc(세계표준시) 기준으로 출력. 1970년 1월 1일 0초부터 지금까지 초단위로 센 값
print(time.strftime("%H:%M:%S", time.localtime(time_now))) # 11:05:43
print("before")
time.sleep(3) # 3초동안 멈췄다가 다음줄로 넘어감.
print("after")
for i in range(10): # 0부터 9까지 10초를 셈(9 출력 후 한번 더 슬립) # 완전 정확한 1초는 아니지만 1초와 매우 유사하게 사용
    print(i)
    time.sleep(1)


# 나중에 각 날짜에 md파일 자동으로 만들어주는 코드 만들기


# math
# 수학 관련
import math
result = math.ceil(1.1) # 올림
print(result) # 2
result = math.floor(1.1) # 내림
print(result) # 1
print(math.pi) # 3.141592.....
# 라디안으로 계산해서 하는 것도 가능


# random
# 난수 관련
import random

# random.random()
random_value = random.random()
print(random_value) # 0.랜덤값
# 0.0 ~ 1.0 사이의 실수 중 난수값

# random.randint(n1, n2)
radnom_value = random.randint(1, 10) # 1 ~ 10의 정수 중 난수값(1, 10 포함)
print(radnom_value)

# random.choice(리스트)
# 리스트의 요소 중 무작위로 하나를 리턴
foods = ["서브웨이", "맥도날드", "짜장면", "국밥", "김치찌개"]
food = random.choice(foods)
print(food)

# random.shuffle(리스트)
li = [1, 2, 3, 4, 5]
random.shuffle(li) # 리스트 순서 바꿈.
print(li)

lotto_numbers = list(range(1, 46)) # 1부터 45의 값 리스트 형태로 생성
for i in range(6):
    print(random.choice(lotto_numbers)) # 6개의 난수값 출력.
# choice 함수는 선택하는 것이기 때문에 중복해서 나올수도 있음

lotto_numbers = list(range(1, 46))
# 이 경우에는 중복되는 값이 나올 경우에 추가하지 않는 것만 하므로 중복값 나오면 출력이 그만큼 덜 됨.
# pop 쓰면 더 나을 듯
# 밑에 처럼 셔플 써서 하는게 가장 나아보임
my_lotto = []
for i in range(6):
    random_value = random.choice(lotto_numbers)
    if random_value not in my_lotto:
        my_lotto.append(random_value)
print(my_lotto)


# in 연산자
# a in b
# a가 b에 포함되어 있으면 True
# a가 b에 포함되어 있지 않으면 False

# not in 연산자
# a not in b
# in이랑 반대

li = [1, 2, 3, 4, 5]
a = 10
for i in li:
    if a == i:
        print("이미 있음")

if a in li:
    print("이미 있음")


# 1 ~ 45까지의 리스트의 순서를 섞어서 앞의 5가지 수를 출력
lotto_numbers = list(range(1, 6))
random.shuffle(lotto_numbers)
my_lotto = lotto_numbers[:6]
print(my_lotto)


"""
색 이름과 음식 이름을 합치면 멋진 밴드 이름이 된다고 합니다.
색 이름과 음식 이름을 무작위로 뽑아
밴드 이름을 추천하는 프로그램을 만들어보세요
"""

import random
colors = ["베이지", "블랙", "블루", "그레이", "핑크", "레드", "그린"]
foods = ["쭈꾸미", "요거트", "오란다", "와플", "아이스티", "떡볶이", "커피"]
band_name = random.choice(colors) + random.choice(foods)
print(band_name)

"""
숫자야구게임 만들기
1. 정답을 정한다. 정답은 4자리 숫자(랜덤)
2. 게임 유저가 정답을 입력한다.
3. 정답과 비교해서 s / b / out 개수 알려준다.
4. 정답을 맞추거나, 종료를 입력하면 끝낸다.
5. 정답을 맞췄을 때 -> 한번 더 하시겠습니까?
"""
import random
numbers = list(range(10))
random.shuffle(numbers)
answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]
# 맨 앞에 0이면 answer = numbers[1:5] 맨 앞이 0이 아닌 False값이면 answer = numbers[:4]


print("""
숫자야구게임
4자리 숫자를 입력해주세요.
그만 하고 싶으면 '종료'를 입력해주세요.
""")
while True:
    user_input = input("정답은? ")
    user_input = user_input.strip() # 공백을 받아도 값을 내고 싶다면
    if user_input[0] == "0":
        print("첫번째 숫자를 0이 아닌 다른 숫자로 입력해주세요.")
        continue
# 만약 중복된 값을 받고싶지 않다면 for문 내에 count 써서 2 이상의 값이 나오면 continue 되도록
    if user_input == "종료":
        print("종료합니다.")
        break
    if user_input.isdecimal(): # 정수일때 트루, 비슷하게 isdigit()이 있는데 이건 숫자로 이뤄지면 트루
        if len(user_input) != 4:
            print("입력이 잘못 되었습니다.")
            continue
    else:
        print("입력이 잘못 되었습니다.")
        continue
    strike = 0
    ball = 0
    out = 0
    for i in range(4):
        input_value = int(user_input[i])
        if input_value not in answer: # 숫자가 없을 때
            out += 1
        elif input_value == answer[i]: # 첫번째 숫자가 있고 자릿수가 맞을 때
            strike += 1
        else: # 첫번째 숫자가 있기는 하나 자릿수가 맞지 않을 때
            ball += 1
    print(f"strike: {strike}, ball: {ball}, out: {out}")

    if strike == 4:
        print("정답!")

        while True:
            user_input = input("한번 더 하시겠습니까? [y/n]")
            if user_input != "y" and user_input != "n":
                print("잘못 입력되었습니다.")
                continue
            break
        if user_input == "n":
            break
        random.shuffle(numbers)
        answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

# 삼항 연산자
# 참일때값 if 조건 else 거짓일때값
result = "참" if True else "거짓"
print(result)

def is_odd_number(n):
    return "홀수" if n % 2 == 1 else "짝수"


# os
# os 자원을 제어, operate system(운영체제)

# import os
# # os.environ
# # 시스템의 환경변수 값을 리턴한다.
# print(os.environ)

# # os.getcwd()
# # get current working directory
# print(os.getcwd()) # 현재 작업위치 리턴. C:\Users\405\my_study

# # os.mkdir(디렉터리)
# # 디렉토리(폴더)를 만든다
# os.mkdir("폴더1") # 현재 작업공간에 폴더가 만들어짐. (마이스터디 폴더에 생성됨.)

# # os.rename(원래이름, 바꿀이름)
# # 파일의 이름을 바꾼다.
# os.rename('파일1', '파일2') # 마이스터디 내의 '파일1' 이 '파일2'로 바뀜

# # os.rmdir(디렉토리)
# # 디렉터리(폴더)를 지운다.
# # 폴더 안에 아무것도 없어야 함(비어있어야 함)
# os.rmdir("폴더1")

# # os.unlink(파일)
# # 파일을 지운다.
# os.unlink('파일2')

# os.path
# # os.path.exists("경로")
# # 파일이 있으면 True, 없으면 False
# if os.path.exists("없는 파일"):
#     f = open("없는파일", "r") # 있으면 '없는파일' 읽기
# else:
#     print("파일이 없습니다.")
#     f = open("없는파일", "w") # 없으면 '없는파일'생성
#     f.close()

# # os.path.join("경로", "경로", "경로")
# # 경로를 합쳐서 1개의 경로로 만들어준다.
# cwd = os.getcwd() # my_study 폴더
# my_folder = "python_study" # 파이썬 폴더
# file_name = "test_file.txt" # 파일명
# file_path = os.path.join(cwd, my_folder, file_name) # my_study/python_study
# with open(file_path, "w", encoding="utf-8") as f: # 경로 합쳐서 python_study에 파일 만듦
#     f.write("테스트 파일을 작성합니다.")


# 외부 라이브러리
# 파이썬 표준 라이브러리가 아닌 라이브러리
# pip를 사용해서 설치한다.
# 예시
# import    numpy, pandas, matplotlib, scikit-learn, keras, Tensorflow, opencv, django, flask, fastapi 등등

# pip
# package installer for python
# 파이썬 모듈, 패키지 설치하는 도구

# PyPI(Python Package Index) 파이썬 소프트웨어 저장 공간
# PyPI에 있는 파이썬 패키지를 설치해준다.

# 최신버전 패키지 설치
# pip install 패키지 이름

# 패키지 삭제
# pip uninstall 패키지 이름

# 특정 버전으로 설치
# pip install 패키지이름==1.0.5

# 최신 버전으로 업그레이드
# pip install --upgrade 패키지 이름

# 설치된 패키지 리스트 확인
# pip list

# numpy 설치함.

# pip freeze 설치기록 저장 같은건데 나중에 따로 알아보기