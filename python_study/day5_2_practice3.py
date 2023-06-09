"""
2 ~ 9 사이의 숫자를 입력받아
해당하는 단의 구구단을 출력하세요.
2 ~ 9 사이의 숫자가 아닌 값이 입력된 경우,
잘못 입력되었다고 출력하고 다시 입력받으세요.
"""

# 강사님 답
n = int(input("몇 단?"))
# if n > 1 and n < 10: # n < 2 or n > 10: 으로 해서 2 ~ 9값이 아닌 경우를 지정해도 됨.
# 파이썬은 if 2 <= n <= 9 처럼 합쳐서 써도 됨.

while not 2 <= n <= 9: # True랑 False를 뒤집기. 결과적으로 2 ~ 9가 아닐 경우 while문 진입
    print("2 ~ 9 사이의 숫자를 입력해주세요.")
    n = int(input("몇 단?"))
for i in range(1, 10): # range9도 가능. 1, 10은 1 ~ 9
    print(n, "*", i, "=", n * i)


# 문자열도 넣었을 때 에러가 안 나게.
li_a = ["2", "3", "4", "5", "6", "7", "8", "9"]
n = input("몇 단: ")
while li_a.count(n) == 0:
    print("2 ~ 9 사이의 숫자를 입력해주세요.")
    n = input("몇 단: ")
n = int(n)
for i in range(1, 10):
    print(n, "*", i, "=", n * i)

# 문자열의 구성을 파악하는 isdecimal() 함수를 쓰면
# 더 간단하게 가능. (문자열 내의 값이 정수로 구성되어 있는지 확인하는 함수.)

"""
정수를 입력받고
그 정수보다 작은 수 중
가장 큰 제곱수를 출력하세요.
2 이상의 정수를 받는다고 했을 때
"""

# 변수 a가 있다고 할 때
# n > a ** 2
# n보다 작은 최대정수가 % 0이 되도록 구해야됨

# 내 답. 이게 젤 나은 듯
n = int(input("정수: "))
a = n
while True:
    a -= 1
    if n > a ** 2:
        break
print(a ** 2)


# 강사님 답
n = int(input("정수: "))
i = 1
while True:
    if i ** 2 >= n:
        break
    answer = i ** 2
    i += 1
print(answer)


# 제곱근을 활용하는 방법도 있음 n ** 0.5


"""
[1, 2, 3, 4, 5]
[10, 20, 30, 40, 50]
[532, 5941, 54682, 58, 5]
3개의 리스트에서 같은 인덱스의
값끼리 더하여 출력하세요.
"""

a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
c = [532, 5941, 54682, 58, 5]
for i in range(len(a)): # 0 ~ 4
    print(a[i] + b[i] + c[i])


# zip()
# 길이가 같은 list를 묶어서 for문 등으로
# 사용 가능한 iterable을 반환한다.
zip(a, b, c)

for x, y, z in zip(a, b, c):
    print(x + y + z)


# while문으로 작성하기
i = 0
while i < 5:
    print(a[i] + b[i] + c[i])
    i += 1


"""
정수를 입력받고 1부터 입력받은
정수까지 모두 출력하세요.
단, 숫자에 3, 6, 9가 들어있는
경우 숫자 대신 짝 이라고 출력하세요.
3의 배수가 아님
"""


n = int(input("정수: "))
for i in range(1, n + 1):
    answer = i # 기본 출력값을 i로 해놓고 if를 통해 짝을 할지 말지 정함.
    for j in str(i): # 문자열로 바꿔서 for문 진행
        if int(j) % 3 == 0 and j != "0": # 앞자리부터 차근차근 확인해서 3이 나올 경우 answer에 짝 할당 후 for문 나감.
            answer = "짝" # 369 중 하나라도 나왔을 때 짝으로 출력하도록
            break # 두번째 for문만 빠져나감.
    print(answer) # 이중 for문 안에 있는 if를 조건에 안 걸리고 통과한다면 처음에 할당한 i가 출력



"""
정수를 입력받고 그 정수의 약수를
모두 출력하세요.
약수: 나누었을 때 나머지가
    0으로 나누어 떨어지게 하는 수
"""

n = int(input("정수: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# while문으로 작성하기
n = int(input("정수: "))
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i += 1