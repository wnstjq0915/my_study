# for문
# 파이썬 for문은 다른언어랑 좀 다르게 생김

"""
for 변수 in iterable값:
    반복할 코드
"""

# iterable한 애들은 인덱싱이랑 슬라이싱 가능함

li_1 = ["one", "two", "three"]
for i in li_1:    # i가 전에 선언이 안 돼있어도 가능
    print(i)

# 첫번째 요소부터 마지막 요소까지
# 변수에 대입하면서 반복

# 리스트의 값이 i에 할당돼서 실행문을 거친 뒤
# 리스트의 두번째 값이 i에 재할당.
# 리스트를 전부 순회할 때까지 반복

s1 = "hello" # 얘도 인덱싱이 가능한 iterable값이므로 한글자씩 가능
for i in s1:
    print(i)

# for문도 for문 내에서 리스트에 append하면 무한반복 가능하지 않나

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse() # 10부터 1까지 출력하게 함
for number in numbers:
    print(number)

# range() 사용법
#숫자 range 객체를 만들어주는 함수
# range(끝 정수)
# 0 ~ 끝 정수 -``
# range(시작, 끝)
# 시작 ~ 끝 -1
# range(시작, 끝, 스텝)
# 시작 ~ 끝 -1까지인데 스텝만큼 차이나게

for i in range(10): # == range(0, 10)
    print(i) # 0 ~ 9 출력

for i in range(1, 10):
    print(i) # 0 ~ 9 출력

for i in range(1, 21, 2):
    print(i) # 1, 3, 5, 7, 9, ... 19 출력. 2는 간격


# for문을 사용하여 2부터 30까지 출력해보세요
# for문을 사용하여 2부터 30까지 중 짝수만 출력해보세요
# for문을 사용하여 10부터 1까지 출력해보세요

for i in range(2, 31):
    print(i)

for i in range(2, 31, 2):
    print(i)

for i in range(2, 31):
    if i % 2 == 0: # 바로 윗코드랑 같음
        print(i)

for i in range(2, 31):
    if i % 2 == 1: # 바로 윗코드랑 같음
        pass
    else:
        print(i)

# if i % 2 == 1 로 호르만 건너뛰는 것도 가능
# if문에서 continue와 비슷한 pass 활용하면 좋음. 아무 동작 안하고 밖으로 빠져나오는 것

# pass 테스트
i = 1
if i == 1:
    pass
print("완료")

for i in range(10, 0, -1):
    print(i)

for i in reversed(range(1, 11)): # reverse는 리스트만 가능해서 reversed로 이용
    print(i)

for i in range(1, 11)[::-1]: # [::-1]에 있는 -1은 방향, 시작인덱스와 끝 인덱스를 비운 슬라이싱은 전체범위
    print(i)


money = 10000
price = 1000
coffee = 5

for i in range(coffee): # range 안에 0부터 4까지 있음. 매우매우매우 중요.
    print("커피를 구매했습니다.")
    money -= price
    print("잔돈:", money, ", 남은 커피:", coffee - 1 - i) # i를 이용한게 포인트
# 이 코드는 잔액은 고려되지 않음

# 마지막에 coffee - 1 - i 에서 -1이 거슬리면 range(1, coffee + 1)로 가능

for i in range(1, coffee + 1): # 1 ~ 5
    print("남은 커피:", coffee - i)
# 위에랑 거의 같으나 print에서 -1을 없앰

for i in range(coffee):
    coffee -= 1
    print("남은 커피:", coffee)
# 위에랑 거의 같으나 print에서 -1을 없앰


for i in range(coffee): # range 안에 0부터 4까지 있음. 매우매우매우 중요.
    print("커피를 구매했습니다.")
    money -= price
    print("잔돈:", money, ", 남은 커피:", coffee - 1 - i)
    if money < price:
        break

"""
while은 조건중시 반복문
for문은 횟수중시 반복문
"""

prices = [500, 700, 930]
money = int(input("돈:"))

for i in range(len(prices)):
    price = prices[i]
    print(money // price)
    print(money % price)

for price in prices:
    print(money // price)
    print(money % price)
# 윗코드와 같으나 훨씬 효율적
# 이게 본래 활용법


#시험점수 받은거 적기
scores = []
for i in range(5):
    score = int(input("시험점수"))
    scores.append(score)


# 이중 for문
# 구구단 다 출력해보기
for i in range(2, 10): # range 내의 변수 바꿀 때 주의하기
    print(i, "단")
    for j in range(1, 10):
        print(i, "*", j, "=", i * j)
    print("----------------")