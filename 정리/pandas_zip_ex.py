"""
판다스(pandas)는 데이터 분석과 관련된 기능을 제공하는 파이썬 라이브러리입니다.
다양한 기능들 중에서, 일부 함수들을 예제와 함께 설명해드리겠습니다.
"""


"""
1. read_csv(): CSV(comma-separated values) 파일을 읽어들이는 함수입니다.
아래 코드는 test.csv 파일을 읽어들이는 예제입니다.
"""
import pandas as pd

df = pd.read_csv('test.csv')


"""
2. drop(): 데이터프레임에서 지정된 축(행 또는 열)을 삭제합니다.
아래 코드는 df 데이터프레임에서 'column1' 열을 삭제하는 예제입니다.
"""
import pandas as pd

df = pd.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6]})
df = df.drop('column1', axis=1)


"""
3. isnull(): 데이터프레임에서 결측값(null, NaN)이 있는 위치를 True로 반환합니다.
아래 코드는 df 데이터프레임에서 결측값이 있는 위치를 확인하는 예제입니다.
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({'column1': [1, 2, np.nan], 'column2': [4, np.nan, 6]})
is_null = df.isnull()


"""
4. fillna(): 데이터프레임의 결측값을 지정된 값으로 대체합니다.
아래 코드는 df 데이터프레임의 결측값을 0으로 대체하는 예제입니다.
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({'column1': [1, 2, np.nan], 'column2': [4, np.nan, 6]})
df = df.fillna(0)


"""
5. groupby(): 데이터프레임을 그룹화하고, 각 그룹에 대한 연산을 수행하는 함수입니다.
아래 코드는 df 데이터프레임을 'column1' 값을 기준으로 그룹화하고,
그룹별 'column2' 값의 평균을 구하는 예제입니다.
"""
import pandas as pd

df = pd.DataFrame({'column1': ['A', 'A', 'B', 'B'], 'column2': [1, 2, 3, 4]})
grouped_df = df.groupby('column1').mean()


"""
pd.read_csv, pd.read_excel
이 함수들은 각각 csv 파일과 excel 파일을 읽어와 pandas DataFrame으로 저장하는 함수입니다. 예를 들어, 다음과 같이 사용할 수 있습니다.
"""
import pandas as pd
df_csv = pd.read_csv('data.csv') # csv 파일 읽어오기
df_excel = pd.read_excel('data.xlsx') # excel 파일 읽어오기


