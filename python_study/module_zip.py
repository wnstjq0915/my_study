# 쓸만한 함수 모아둘 예정
class Calculator:
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    def add_many(*args): # 수정해서 사칙연산 다 가능하게
        result = 0
        for i in args:
            result += i
        return result