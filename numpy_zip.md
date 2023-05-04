# numpy 함수 모음
- import numpy as np: 넘피 불러오기.
- np.array(리스트, 튜플, range 등):  리스트나 튜플을 배열로 바꿔 생성합니다.
- np.arange(n1, n2, n3): 지정된 범위 내의  
일정한 간격으로 배열을 생성합니다. 
(rangem()랑 받는 매개변수 같음.)
- .size: 배열에 있는 원소의 전체 갯수
- .shape: 배열의 형태(반환값은 튜플형태)
- .ndim: 배열의 차원 갯수
- .dtype: 배열에 담긴 원소의 자료형 확인
- np.zeros(n1): 0으로 이뤄진 원소n1개짜리 배열 생성
- np.ones(n1, n2): 1로 이뤄진 n1행, n2열 배열 생성
- np.full((n1, n2), n3): n1/n2의 행/렬 구조를 가진 n3으로만 이뤄진 배열 생성
- np.linspace(n1, n2, n3): n1부터 n2(인덱스 아닌거 주의)까지 n3개로 이뤄진 배열 생성
- np.sum(a1, axis=차원): 배열 a1의 차원끼리 값을 더합니다. axis가 없을 경우 모든 값을 더합니다.
- np.concatenate((a1, a2), axis=차원): a1과 a2의 배열을 같은 차원끼리 합침.(axis 기본값 0)
- np.hstack([a1, a2]): a1과 a2의 배열을 같은 차원끼리 axis=1?로 합침

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