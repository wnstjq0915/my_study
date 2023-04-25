"""
계산기 만들기
기능: 두 정수의 사칙연산(+, -, *, /)
add(), sub(), mul(), div(), 함수의 정의
input() 함수를 활용하여
정수 2개, 사칙연산 선택을 입력받은 후
계산 결과를 print한다.
계산식과 결과를
calculator_result.txt파일에 기록한다.
사용자가 'q'를 입력하면 종료한다.
"""
# 내 답 + 강사님 수정

def add(a, b):
    return "%d + %d = %d\n" % (a, b, a + b)
def sub(a, b):
    return "%d - %d = %d\n" % (a, b, a - b)
def mul(a, b):
    return "%d * %d = %d\n" % (a, b, a * b)
def div(a, b):
    return "%d / %d = %d\n" % (a, b, a / b)

d = {
    "1" : add,
    "2" : sub,
    "3" : mul,
    "4" : div,
} # d 안에 add(a, b) 같이 함수를 넣으면 딕셔너리를 읽는 과정에서 함수를 호출하므로 비효율
while True:
    print("""
    계산기
    1: +
    2: -
    3: *
    4: /
    q: 종료
    """)
    operator = input("원하는 연산자를 입력하세요: ")
    if operator == 'q':
        break
    a = int(input("정수 1: "))
    b = int(input("정수 2: "))
    result = d[operator](a, b) # d[operator] 가 add로 변환되면서 함수호출. # 함수호출과정 이해하기
    print(result)
    with open("python_study/calculator.txt", "a", encoding="utf-8") as f:
        f.write(result)


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # 강사님 답

def add(a, b):
    result = str(a) + " + " + str(b) + " = " + str(a + b) + "\n"
    print(result)
    with open("python_study/calculator.txt", "a", encoding="utf-8") as f:
        f.write(result)

def sub(a, b):
    result = str(a) + " - " + str(b) + " = " + str(a - b) + "\n"
    print(result)
    with open("python_study/calculator.txt", "a", encoding="utf-8") as f:
        f.write(result)

def mul(a, b):
    result = str(a) + " * " + str(b) + " = " + str(a * b) + "\n"
    print(result)
    with open("python_study/calculator.txt", "a", encoding="utf-8") as f:
        f.write(result)

def div(a, b):
    result = str(a) + " / " + str(b) + " = " + str(a / b) + "\n"
    print(result)
    with open("python_study/calculator.txt", "a", encoding="utf-8") as f:
        f.write(result)


while True:
    print("""
    계산기
    1: +
    2: -
    3: *
    4: /
    q: 종료
    """)
    operator = input("원하는 숫자를 계산을 입력하세요: ")
    if operator == 'q':
        break
    a = int(input("정수 1: "))
    b = int(input("정수 2: "))
    if operator == "1":
        add(a, b)
    if operator == "2":
        sub(a, b)
    if operator == "3":
        mul(a, b)
    if operator == "4":
        div(a, b)