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

### for - else , while - else문
- break를 써서 반복문을 빠져나오지 않으면 else를 진행.