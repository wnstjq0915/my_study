# pandas 모음
- import pandas as pd
- 행은 Index, 열은 Columns

## pandas 시스템
- df[컬럼] = '값'으로 컬럼의 값들을 한번에 '값'으로 변경할 수 있음.
- min(), max(), mean() 등 기존에 쓰던거 다 되며, 반복문이 안에 내장되어 있어 한번에 값을 구하기 좋음.
- 문자열값에 특정 문자열이 들어있는지 in으로 확인 가능.

## pandas 데이터 호출
- df['컬럼 이름']: 이름으로 행 가져오기.
- df.columns['인덱스']: 인덱스로 행 가져오기.
- df.loc['인덱스 이름']: 이름으로 열 가져오기.
- df.iloc[인덱스]: 인덱스로 열 가져오기.
ex: [1, 2]를 한다면 1행 2열을 가져올 수 있으며, iloc[0, ]을 한다면 0행의 모든 데이터를 가져옴.
## pandas 함수
### pd.함수
- pd.read_csv('경로'): csv파일 열기.(같은 방식으로 엑셀도 가능.)
- pd.read_csv('경로', index_col=0): csv파일 열기.(맨 앞 인덱스값 삭제하며 불러오기)
- pd.DataFrame(): 데이터프레임 생성  
ex  
```python
df = pd.DataFrame({'column1': ['A', 'A', 'B', 'B'], 'column2': [1, 2, 3, 4]}, index=['1', '2', '3', '4'])
```
### df.함수
- df[조건]: 조건을 만족하는 df만 가져옴  
ex: df[df['age'] >= 20]이면 성인만 있는 df를 가져옴
- df[컬럼] == 조건: 조건을 만족하지 True와 False를 보여주는 시리즈를 리턴
- df[컬럼].isin([값1, 값2]): 컬럼이 값1 또는 값2일 경우 True를 주는 시리즈 리턴
- df.head('숫자'): 숫자만큼 행 출력. 기본값 5
- df.rename(columns={'바꾸기 전':'바뀐 후'}): 컬럼값 바꾸기. index도 같은 방식
- df.set_index(df['인덱스로 할 컬럼'], inplace=True): 인덱스를 컬럼값으로 바꾼다.
- df.drop('바꿀 행값 or 열값', axis=x, inplace=True): 행이나 열을 통째로 지운다.
- df.isnull(): 값이 없으면 True, 없으면 False인 df를 보여줌.  
보통 df.isnull().sum()으로 결측치가 얼마나 있는지 확인 <-> 반대는 .notna(), notnull()  
- df.fillna('바꾸고 싶은 값'): df의 NaN값을 바꾸고 싶은 값으로 바꿈.
- df.describe(): df의 데이터 수 확인
- df[값].unique(): 컬럼의 값의 종류를 다 확인
- df[값].nunique(): 컬럼의 값이 몇종류인지 확인
- df.value_counts(): 컬럼의 각 값들이 몇 개씩 있는지 시리즈로 반환
- df[컬럼].values: 컬럼의 각 값을 리스트로 반환. () 없는거 주의
- df.size: df의 크기 확인
- df.apply(func, axis=x): 각 열이나 행에 각각 함수를 적용시키고 싶을 때 사용
- df[컬럼].sort_index(ascending=True): 값을 오름차순 정렬
- df.sort_values('컬럼'): 컬럼을 기준으로 데이터프레임 형태로 정렬. df[컬럼].sort_values()하면 시리즈 형태로 나옴.
- df.astype('타입'): 원하는 타입으로 변경(인플레이스 해야함.)
- df.corr(numeric_only=True): 각 컬럼의 상관계수를 데이터프레임화  
numeric_only=True는 숫자로 되어있는 컬럼만 계산하도록 한 것이며, 필수 아님

### df groupby(내용이 많아서 따로)
- df.groupby(컬럼명): 컬럼 하나를 인덱스로 만들고 데이터 분석함. .agg()를 통해 다중통계를 할 수 있음.  
[예시있음]  
참고할 주소: https://teddylee777.github.io/pandas/pandas-groupby/  
.agg()에 적용할 수 있는 통계함수 문자열 표  

함수 | 내용
------|----
count | 데이터의 개수
sum | 합계
mean | 평균
median | 중앙값
var, std | 분산, 표준편차
min, max | 최소, 최대값
unique, nunique | 고유값, 고유값 개수
prod | 곲
first, last | 첫째, 마지막값