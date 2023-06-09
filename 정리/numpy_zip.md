# numpy 함수 모음
- import numpy as np: 넘피 불러오기.
- .size: 배열에 있는 원소의 전체 갯수
- .shape: 배열의 형태(반환값은 튜플형태)
- .ndim: 배열의 차원 갯수
- .dtype: 배열에 담긴 원소의 자료형 확인
- .sum(axis=차원): 배열 a1의 차원끼리 값을 더합니다. axis가 없을 경우 모든 값을 더합니다.
- .transpose(): 한 배열의 열끼리 합친 배열 생성(axis 설정 가능)
- .flatten(): 1d 배열로 만듦
- .T : 배열의 행렬을 바꿈.
- .mean(axis=x): axis=0이면 같은 열끼리 평균내고, axis=1이면 같은 행끼리 평균
- .reshape(n1, n1): n1행 n2열의 형태로 바꿈. 변수 갯수는 n1*n2 갯수여야 함(빈 공간 X)
- np.array(리스트, 튜플, range 등):  리스트나 튜플을 배열로 바꿔 생성합니다.
- np.arange(n1, n2, n3): 지정된 범위 내의  
일정한 간격으로 배열을 생성합니다. 
(rangem()랑 받는 매개변수 같음.)
- np.zeros(n1): 0으로 이뤄진 원소n1개짜리 배열 생성
- np.ones(n1, n2): 1로 이뤄진 n1행, n2열 배열 생성
- np.full((n1, n2), n3): n1/n2의 행/렬 구조를 가진 n3으로만 이뤄진 배열 생성
- np.linspace(n1, n2, n3): n1부터 n2(인덱스 아닌거 주의)까지 n3개로 이뤄진 배열 생성
- np.concatenate((a1, a2), axis=차원): a1과 a2의 배열을 같은 차원끼리 합침.(axis 기본값 0)
- np.hstack([a1, a2]): a1과 a2의 배열을 같은 차원끼리 axis=1?로 합침
- np.vstack([a1, a2]): 배열을 세로로 쌓기, 동일한 수의 열이 아닐 경우 에러
- np.column_stack([a1, a2]): 배열의 같은 열끼리 합침
- np.random.choice(li_1, n): 랜덤한 값을 복사함. li_1은 이터러블값, n은 선택할 변수 갯수
- np.floor(a1): 배열 내 값의 소수점 버리기
- np.maximum(a1, a2): 같은 원소에서 가장 큰값
- np.subtract(a1, a2): a1원소를 a2원소로 빼기
- np.multiply(a1,a2) #같은 원소끼리 곱셈
- np.where(조건, 값1, 값2): 조건을 만족하는 값을 값1로 채워넣고, 만족하지 못하면 값2를 채움
- .sort(): 오름차순 정렬
- -np.sort(-a1): 내림차순 정렬
- np.eye(n1, n2): 대각 원소 1이고 나머지는 0인 배열 생성. n1, n2를 행/렬로 받고, n1만 있을 경우 n1을 행으로 받음
- np.diag(a1): a1의 대각 원소를 모아서 하나의 배열을 만듦
- np.diag([n1, n2, n3]): 대각 원소가 n1, n2, n3이고 나머지가 0으로 채워진 배열 생성
- np.multiply(a1, a1): a1의 각 원소를 제곱함
- np.dot(a,a): 행렬의 곱

# numpy 특성
- 인덱싱 및 슬라이싱 가능.
- type == numpy.ndarray
- 깊은복사를 피해 얕은복사를 하기 위해선 배열.copy()를 이용하기.
- 벡터화: 배열은 for문 없이 데이터 일괄처리 가능.
```python
# ex
a = np.array([1, 2, 3])
print(a + 2) # [3 4 5]
print(10 - a) # [9, 8, 7]
print(a * a) # [1, 4, 9]
```
- 2차원에서는 axis=0은 열끼리 진행(세로로만), axis=1은 행끼리(가로로만) 진행
```python
# ex
c = np.array([[0,1,2],[3,4,5]])
d = np.array([[6,7,8],[9,10,11]])
print(np.concatenate((c,d),axis=0))
print(np.concatenate((c,d),axis=1))
"""
axis0
[[ 0  1  2]
[ 3  4  5]
[ 6  7  8]
[ 9 10 11]]

axis1
[[ 0  1  2  6  7  8]
[ 3  4  5  9 10 11]]
"""
```
- numpy는 인덱싱에 조건을 줄 수 있음.
```python
# ex
Arr = np.arange(0,21) # 0 ~ 20까지 생성
Arr1 = Arr[Arr%2==0] # [0, 2, 4, 6, 8, ...]
Arr2 = Arr[Arr%2!=0] # [1, 3, 5, 7, 9, ...]
```
- 슬라이싱을 통해 한번에 값 변경 가능
```python
arr1d = np.arange(8) # 0 ~ 7 값 생성
arr1d[3:6]=100 # [0, 1, 2, 100, 100, 100, 6, 7]
```
- 접근이 자유로움
```python
arr2d = np.arange(20).reshape(4,-1)
""" 배열 생성
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
"""
arr2d[1][2] #재귀적 접근 / 1행 2열, 7 접근
arr2d[1,2] #컴마를 이용하여 쉽게 인덱싱을 할 수 있음. 7 접근
arr2d[:3][:2] # 3행까지, 2열까지 접근
""" [:3][:2]
array([[ 0,  1],
       [ 5,  6],
       [10, 11]])
"""
arr2d[[0,2]] #0행과 2행 #multi index는 []하나 더 추가해야함.
"""[[0,2]]
array([[ 0,  1,  2,  3,  4],
       [10, 11, 12, 13, 14]])
"""
arr2d[[0,3],[4]] # 0인덱스 행과 3인덱스 행의 인덱스 4인 [4, 9]에 접근
arr2d[[0,1],[4,3]] # 0인덱스 행의 4인덱스 열, 1인덱스 행의 3인덱스 열인 [4, 8] 접근
arr = np.array([0,1,2,3,4]) # 새로 0 ~ 4 배열 생성
arr[[True,False,True,False,True]] # boolean을 통한 접근. [0, 2, 4] 접근
```
