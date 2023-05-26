# pandas 모음
- import pandas as pd
- 행은 Index, 열은 Columns

## pandas 시스템
- df[컬럼] = '값'으로 컬럼의 값들을 한번에 '값'으로 변경할 수 있음.
- min(), max(), mean() 등 기존에 쓰던거 다 되며, 반복문이 안에 내장되어 있어 한번에 값을 구하기 좋음.

## pandas 데이터 호출
- df['컬럼 이름']: 이름으로 행 가져오기.
- df.columns['인덱스']: 인덱스로 행 가져오기.
- df.loc['인덱스 이름']: 이름으로 열 가져오기.
- df.iloc[인덱스]: 인덱스로 열 가져오기.
ex: [1, 2]를 한다면 1행 2열을 가져올 수 있으며, iloc[0, ]을 한다면 0행의 모든 데이터를 가져옴.
## pandas 함수
- pd.read_csv('경로'): csv파일 열기.(같은 방식으로 엑셀도 가능.)
- pd.read_csv('경로', index_col=0): csv파일 열기.(맨 앞 인덱스값 삭제하며 불러오기)
- df[조건]: 조건을 만족하는 df만 가져옴
ex: df[df['age'] >= 20]이면 성인만 있는 df를 가져옴
- df[컬럼] == 조건: 조건을 만족하지 True와 False를 보여주는 시리즈를 리턴
- df[컬럼].isin([값1, 값2]): 컬럼이 값1 또는 값2일 경우 True를 주는 시리즈 리턴
- df.head('숫자'): 숫자만큼 행 출력. 기본값 5
- df.rename(columns={'바꾸기 전':'바뀐 후'}): 컬럼값 바꾸기. index도 같은 방식
- df.set_index(df['인덱스로 할 컬럼'], inplace=True): 인덱스를 컬럼값으로 바꾼다.
- df.drop('바꿀 행값 or 열값', axis=x, inplace=True): 행이나 열을 통째로 지운다.
- df.isnull(): 값이 없으면 True, 없으면 False인 df를 보여줌. 보통 df.isnull().sum()으로 결측치가 얼마나 있는지 확인 <-> 반대는 .notna(), notnull()
- df.describe(): df의 데이터 수 확인
- df[값].unique(): 컬럼의 값의 종류를 다 확인
- df[값].nunique(): 컬럼의 값이 몇종류인지 확인
- df[컬럼].values: 컬럼의 값들을 리스트로
- df.grupby(컬럼명): 컬럼 하나를 인덱스로 만들고 데이터 분석?
- https://teddylee777.github.io/pandas/pandas-groupby/
- 