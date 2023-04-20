"""
while 조건:
    반복할 코드
"""
# 조건이 참인 경우에 코드를 계속 반복

n = 1
while n <= 10:
    print(n)
    n += 1 # 10까지 출력, 11이 되고 실행되지 않음.
print(n) # 10 출력하고 ++했기에 11 출력

# 주석 단축키
# 컨트롤 k -> 컨트롤 c = 주석 ( 컨/와 다르게 주석에 한번 더 하면 #가 추가될 뿐)
# 컨트롤 k 0> 컨트롤 u = 주석 없애기

# += 연산자
# 대입 연산자의 일종
# 더하기 연산 후 할당
# n += 1 은 n = n + 1이라는 의미
# 다른 산술연산자 다 적용 가능

# # s1 = '안녕'
# # s1 += '하세요'
# # print(s1) # 안녕하세요


# 10부터 1까지 출력하세요

n = 10
while n >= 1: # > 0 도 됨. 주석 방법이 더 편해보임
    print(n)
    n -= 1


money = 10000
price = 1000
coffee = 5
while money >= price: # money - price >= 0:도 가틍
    print("커피를 구매했습니다.")
    money -= price
    coffee -= 1
    print("남은 커피:", coffee) # 문자열값과 정수값 같이 사용
    if coffee == 0: # coffee가 0이 되면 브레이크
        break

# break
# 반복문을 즉시 종료한다.

# 커피를 n번 구매했습니다로 출력해보기 (if 연습)
money = 10000
price = 1000
if money >= price:
    print("커피를 " + str(money // price) + "번 구매했습니다.")
else:
    print("커피를 구매하지 못 했습니다.")


# while 반복문을 활용하여
# 1부터 10까지 홀수만 출력한다.

a = 1
while a <= 10:
    if a % 2 == 1:
        print(a)
    a += 1

# 다른 방법도 있음
# continue
# 반복문의 제일 처음으로 돌아감

a = 1
while a <= 9:
    a += 1
    if a % 2 == 0:
        continue # 짝수면 맨 처음으로 돌아감
    print(a)



# 무한 반복문
# 무한 루프
# 조건식에 True를 입력해 항상
# 참이 되도록 하여 무한히 반복하게 한다.
# 콘솔창에 컨트롤c하면 실행 강제종료

while True:
    user_input = input("종료하려면 1을 입력해주세요.")
    print(user_input)
    if user_input == "1": # input값은 문자열인거 주의
        break


# 무한반복문으로 계산기 만들기
# +, -, *, / 계산
# 2개의 수를 계산 a + b

# # while True:
# #     print("""
# #     계산기
# #     =======
# #     1. 더하기(+)
# #     2. 빼기(-)
# #     3. 곱하기(*)
# #     4. 나누기(/)
# #     """)
# #     operator = int(input("계산을 선택하세요 : "))
# #     if operator == 1:
# #         print("1 + 2 =", 1 + 2)
    
# #     if operator == 2:
# #         print("1 - 2 =", 1 - 2)
    
# #     if operator == 3:
# #         print("1 * 2 = ", 1 * 2)
    
# #     if operator == 4:
# #         print("1 / 2 = ", 1 / 2)

# elif는 else와 if를 합친것


# 계산기 만들어보기
# input 안에서 계산 안 되는거 주의
while True:
    print("""
계산기
=========================================
숫자 a, 연산자, 숫자 b 순으로 입력해주세요.
도중에 종료하려면 q를 입력해주세요.
""")
    input_a = input("숫자 a를 입력해주세요: ")
    if input_a == "q":
        break
    print("현재까지 입렵된 값:", input_a)
    while True:
        input_oper = input("연산자를 입력해주세요: ")
        if input_oper == "*":
            print("현재까지 입렵된 값:", input_a, "x")
            break
        elif input_oper == "+" or input_oper == "-" or input_oper == "/":
            print("현재까지 입렵된 값:", input_a, input_oper)
            break
        else: 
            continue
    if input_oper == "q":
        break
    input_b = input("숫자 b를 입력해주세요: ")
    if input_b == "q":
        break
    input_a = int(input_a)
    input_b = int(input_b)
    if input_oper == "+":
        print("결과:", input_a, "+", input_b, "=", input_a + input_b)
    if input_oper == "-":
        print("결과:", input_a, "-", input_b, "=", input_a - input_b)
    if input_oper == "*":
        print("결과:", input_a, "x", input_b, "=", input_a * input_b)
    if input_oper == "/":
        print("결과:", input_a, "/", input_b, "=", input_a / input_b)
    if input("""====================================
계산을 종료하려면 q를 입력해주세요.
계속하려면 아무거나 입력해주세요.
""") == "q":
        break
    else:
        continue


# 사용자가 가지고 있는 돈을 입력받는다.
# 구매할 수 있는 커피의 개수와 잔돈을 출력한다.
# 구매할 수 있는 음료수의 개수와 잔돈을 출력한다.
# 구매할 수 있는 콜라의 개수와 잔돈을 출력한다.
# 커피는 500원, 음료수는 700원, 콜라는 930원
# 물품의 개수는 무한하다고 가정한다.
# while 반복문을 사용하여 작성한다.

idx = 0
prices = [500, 700, 930]
money = int(input("돈: "))
while idx < len(prices):
    price = prices[idx]
    print("구매할 수 있는 수:", money // price, "개, 잔돈:", money % price, "원")
    idx += 1


# while 반복문을 사용해서
# scores 리스트에 시험 점수 5개를
# 정수형으로 입력받으세요.

# i = 0
# scores = []
# while i < 5:
#     scores.append(int(input("시험점수: ")))
#     i += 1
# print(scores)


# while 반복문을 사용하여
# 구구단 2단을 출력하세요.

i = 1
while i < 10:
    print(2 * i)
    i += 1