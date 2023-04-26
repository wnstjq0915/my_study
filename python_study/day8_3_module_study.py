# # 모듈
# # 함수, 변수, 클래스 모아놓은 파이썬 파일
# # 다른 파이썬 프로그램에서 불러와서 사용
# # import 명령어로 불러옴

"""
import 모듈이름
"""
import my_module
print(my_module.add(1, 2))
print(my_module.sub(1, 2))

"""
from 모듈이름 import 모듈함수
from 모듈이름 import 모듈함수1, 모듈함수2
from 모듈이름 import *          -> 별은 전체 다
"""
from my_module import add, sub
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(add(1, 2))
print(sub(1, 2))
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
from my_module import *
print(add(1, 2))
print(sub(1, 2))
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# import my_module # 함수를 뒤에 붙이지 않으면 코드가 한번 다 실행되면서 불러옴. 

from day8_2_my_calculator import MyCalculator
# my_calculator = MyCalculator()
# my_calculator.div(10, 0) # 컨트롤하고 div를 누르면 함수위치로 이동.
# 에러가 나면 그 즉시 프로그램이 중단되기 때문에(밑에 코드 실행X) 에러는 나지 않게 하는게 중요

class ZeroCalculator(MyCalculator):
    def div(self, n1, n2):
        if n2 == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            print(f"{n1} / {n2} = {n1 / n2}")

zero_calculator = ZeroCalculator()
zero_calculator.div(10, 0)