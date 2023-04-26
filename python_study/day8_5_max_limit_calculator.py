"""
Mycalculator 모듈의 클래스를 상속받아서 MaxLimitCalculator 클래스를 정의하세요.
add, sub, mul, div 메소드를 사용하여 더하기, 빼기, 곱하기, 나누기를 할 수 있다.
0으로 나눴을 때 에러가 발생하지 않도록 처리한다.
입력되는 정수가 1개라도 100보다 크면 계산하지 않고
100 이하의 값을 입력하도록 안내 메세지를 출력한다.
계산 결과가 100보다 크면 계산하지 않고 100 이하의 결과가 나오는 값을 입력하도록 안내 메세지를 출력한다.
"""

from day8_2_my_calculator import MyCalculator

class MaxLimitCalculator(MyCalculator):
    def add(self, n1, n2):
        if n1 > 100 or n2 > 100:
            print("100 이하의 정수를 입력해주세요.")
        else:
            if n1 + n2 > 100:
                print("계산결과가 100 이하가 나오도록 입력해주세요.")
            else:
                print(f"{n1} + {n2} = {n1 + n2}")

    def sub(self, n1, n2):
        if n1 > 100 or n2 > 100:
            print("100 이하의 정수를 입력해주세요.")
        else:
            print(f"{n1} - {n2} = {n1 - n2}")

    def mul(self, n1, n2):
        if n1 > 100 or n2 > 100:
            print("100 이하의 정수를 입력해주세요.")
        else:
            if n1 * n2 > 100:
                print("계산결과가 100 이하가 나오도록 입력해주세요.")
            else:
                print(f"{n1} * {n2} = {n1 * n2}")
    
    def div(self, n1, n2):
        if n1 > 100 or n2 > 100:
            print("100 이하의 정수를 입력해주세요.")
        else:
            if n2 == 0:
                print("0이 아닌 값을 입력해주세요.")
            else:
                print(f"{n1} / {n2} = {n1 / n2}")

a, b = int(input("정수1: ")), int(input("정수2: "))
max_limit_calculator = MaxLimitCalculator()
max_limit_calculator.div(a, b)