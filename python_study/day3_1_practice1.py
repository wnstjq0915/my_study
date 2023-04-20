# """
# eng 변수, kor 변수, math 변수를 만들고
# 각 변수는 과목의 시험 점수이다.
# 영어 점수는 80점
# 국어 점수는 60점
# 수학 점수는 50점
# 3과목 점수의 평균을 내고
# 평균 점수에 따라 성적을 출력한다.
# A : 91 ~ 100
# B : 81 ~ 90
# C : 71 ~ 80
# D : 61 ~ 70
# F : 60 이하
# """

eng = int(input("영어 점수:")) # 인풋으로 받은 문자열값을 정수형으로 변환
kor = input("국어 점수:")
math = int(input("수학 점수:"))

kor = int(kor) # 이렇게도 변환 가능

avg = (eng + kor + math) / 3
print(f"평균점수: {avg}")

if avg >= 91:
    print("성적: A")
elif avg >= 81:
    print("성적: B")
elif avg >= 71:
    print("성적: C")
elif avg >= 61:
    print("성적: D")
else:
    print("성적: F")

# 연산이 적을수록 속도가 빠르기 때문에
# avg라는 변수를 만들고 각 조건에 avg를 대입하는 것이 효율적
# (나중에 다른 과목을 추가해서 평균을 구하기도 용이)

# input() 함수
# 사용자로부터 정보를 입력받는 함수
# input() 함수는 무조건 Sring값으로 변환됨

# 정수형 변환 함수
# 정수형, integer형, int형
# int(값)

# user_input = input()
# print(f"출력: {user_input}") # 터미널창에 입력하면 출력해줌