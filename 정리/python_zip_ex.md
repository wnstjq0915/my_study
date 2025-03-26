# python_zip 예시

## list
- zip  

```python
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
c = [532, 5941, 54682, 58, 5]

for i in range(len(a)): # 0 ~ 4
    print(a[i] + b[i] + c[i])

# 위의 for문을 zip()함수를 이용해 표현 가능

for x, y, z in zip(a, b, c):
    print(x + y + z)
```

## 딕셔너리
```python
"""
컷트라인이 60점일 때, 사람이름과 통과여부를 리스트로
담아서 출력하라. 이름과 통과여부는 튜플로 묶여있는 자료.
(이름, 통과여부)
"""

# 딕셔너리 활용문제.
# 주어진 값
students = {
    "보라돌이": 61, 
    "뚜비": 35,
    "나나": 78,
    "뽀": 88
}
# 답: 
answer = [(i, "통과") if j >= 60 else (i, "미통과") for i, j in students.items()]
print(answer)
```

## 반복문
### while문
```python
i = 0
while i < 10 # 10번 반복
    """
    실행문
    i += 1
    """
```
- 조건반복 특화
- 무한반복 가능(While True:)

### for문
```python
for i in range('반복할 횟수')
# range 대신 iterable 값을 넣어도 됨.(리스트, 문자열 등등)
    """
    실행문
    """
```
- 횟수반복 특화

### 한줄for문
실행문/리턴값 for i in iterable값

### for - else , while - else문
- break를 써서 반복문을 빠져나오지 않으면 else를 진행.

### 반복문을 쓰지 않은 함수 내 반복
```python
#재귀적으로 하는 것.
def fact(n): # 팩토리얼 함수. 5를 받으면 5*4*3*2*1 값 리턴
    if n<=1: #n이 1이하이면 종료조건
        return 1
    return n*fact(n-1)
```
## lambda 활용
- lambda는 함수로만 사용되지 않음.

### map
- lambda가 함수로 사용
```python
map(함수명(또는 람다), 이터러블값) # 각 요소에 함수가 적용된 이터러블값
```
- lambda 사용하게 되면
```python
answer = list(map(lambda x: x ** 2, range(5)))
# (0, 1, 2, 3, 4) 각 값에 순서대로 lambda 함수 적용
print(answer) # [0, 1, 4, 9, 16]
```

### filter
- lambda가 조건으로 사용
```python
filter(람다조건, 이터러블값) # -> 조건을 만족하는 요소를 가진 이터러블값
```
```python
answer = list(filter(lambda x: x < 5, range(10)))
# (1, 2, ... 8, 9) 값에 lambda 조건을 만족하는 값만 리턴
print(answer) # [0, 1, 2, 3, 4]
```

### reduce
- 값의 누적이 필요할 때 사용
```python
from functools import reduce
reduce(lambda(값을 누적할 변수, 이터러블값을 읽기 위한 요소: 실행코드, 이터러블값)
```
- 기본사용
```python
from functools import reduce
answer = reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
print(answer) # 10
```
- 문자열에 사용1
```python
from functools import reduce
answer = reduce(lambda x, y: x + y, 'abcde')
print(answer) # 'abcde'
```
- 문자열에 사용2
```python
from functools import reduce
answer = reduce(lambda x, y: x + y.upper(), 'abcde')
print(answer) # 'aBCDE'
```
#### 역순진행
- 인덱싱에서 슬라이싱에서 ::-1 하는 것과 같이 반대로 진행 가능
- 문자열에 사용1
```python
from functools import reduce
answer = reduce(lambda x, y: y + x, 'abcde')
print(answer) # 'edcba'
```
- 문자열에 사용2
```python
from functools import reduce
answer = reduce(lambda x, y: y + x.upper(), 'abcde')
print(answer) # 'eDCBA'
```
