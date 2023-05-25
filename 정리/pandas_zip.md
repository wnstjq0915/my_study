# pandas 모음
- import pandas as pd
- 행은 Index, 열은 Columns

## pandas 데이터 호출
- df['컬럼 이름']: 이름으로 행 가져오기.
- df.columns['인덱스']: 인덱스로 행 가져오기.
- df.loc['인덱스 이름']: 이름으로 열 가져오기.
- df.iloc[인덱스]: 인덱스로 열 가져오기.
ex: [1, 2]를 한다면 1행 2열을 가져올 수 있으며, iloc[0, ]을 한다면 0행의 모든 데이터를 가져옴.
- pd.read_csv('경로'): csv파일 열기.(같은 방식으로 엑셀도 가능.)
- df.head('숫자'): 숫자만큼 행 출력. 기본값 5
- pd.read_csv('경로', index_col=0): csv파일 열기.(맨 앞 인덱스값 삭제하며 불러오기)
- df.rename(columns={'바꾸기 전':'바뀐 후'}): 컬럼값 바꾸기. index도 같은 방식
- df[조건]: 조건을 만족하는 df만 가져옴
ex: df[df['age'] >= 20]이면 성인만 있는 df를 가져옴
- df[컬럼] == 조건: 조건을 만족하지 True와 False를 보여주는 시리즈를 리턴
- df[컬럼].isin([값1, 값2]): 컬럼이 값1 또는 값2일 경우 True를 주는 시리즈 리턴