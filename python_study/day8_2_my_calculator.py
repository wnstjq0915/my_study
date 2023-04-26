"""
7일차 만든 계산기 클래스를 사용해 리메이크하기
add, sub, mul, div 메소드
"""
class MyCalculator: # 나중에 if로 수정
    def add(self, n1, n2):
        print(f"{n1} + {n2} = {n1 + n2}")
    def sub(self, n1, n2):
        print(f"{n1} - {n2} = {n1 - n2}")
    def mul(self, n1, n2):
        print(f"{n1} * {n2} = {n1 * n2}")
    def div(self, n1, n2):
        print(f"{n1} / {n2} = {n1 / n2}")
if __name__ == "__main__":
    my_calculator = MyCalculator()
    while True:
        print("계산기\n--------------\n1: +\n2: -\n3: *\n4: /\nq: 종료")
        operator = input("계산방법: ")
        if operator == 'q':
            break
        if operator == "1" or operator == "2" or operator == "3" or operator == "4":
            n1, n2 = int(input("정수1: ")), int(input("정수2: "))
            a = {"1": my_calculator.add, "2": my_calculator.sub, "3": my_calculator.mul, "4": my_calculator.div}
            a[operator](n1, n2) # if문 대신 이렇게도 가능하나 if문이 가독성이 더 뛰어남. if문 12줄, 이거 7줄. 걍 if문 쓰기
            continue
        print("잘못입력했습니다.")
        # my_calculator = MyCalculator()
        # if operator == "1":
        #     my_calculator.add(n1, n2)
        # elif operator == "2":
        #     my_calculator.sub(n1, n2)
        # elif operator == "3":
        #     my_calculator.mul(n1, n2)
        # elif operator == "4":
        #     my_calculator.div(n1, n2)
        # else:
        #     print("잘못입력했습니다.")