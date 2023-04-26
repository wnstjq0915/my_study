"""
7일차 만든 계산기 클래스를 사용해 리메이크하기
add, sub, mul, div 메소드
"""
class MyCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        print("%d + %d = %d" % (self.a, self.b, self.a + self.b))
    def sub(self):
        print("%d - %d = %d" % (self.a, self.b, self.a - self.b))
    def mul(self):
        print("%d * %d = %d" % (self.a, self.b, self.a * self.b))
    def div(self):
        print("%d / %d = %d" % (self.a, self.b, self.a / self.b))
while True:
    print("계산기\n--------------\n1: +\n2: -\n3: *\n4: /\nq: 종료")
    operator = input("계산방법: ")
    if operator == 'q':
        break
    n1 = int(input("정수1: "))
    n2 = int(input("정수2: "))
    my_calculator = MyCalculator(n1, n2)
    if operator == "1":
        my_calculator.add()
    if operator == "2":
        my_calculator.sub()
    if operator == "3":
        my_calculator.mul()
    if operator == "4":
        my_calculator.div()