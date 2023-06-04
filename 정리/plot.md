# 데이터 시각화 정리

## 관련 라이브러리
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import platform # 한글폰트 사용
platform.platform()
platform.system() # 윈도우는 'Windows', 맥은 'Darwin'
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows
# matplotlib.rcParams['font.family'] = 'AppleGothic' # Mac
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결
```

## 시각화
### hist
```python
df['컬럼'].hist()
# or
df['컬럼'].hist(bins=숫자) # bins를 높이면 데이터 세밀화
```
- 컬럼의 값을 히스토그램으로

### countplot
```python
sns.countplot(data=df, x = '컬럼')
plt.show()
```
- df[컬럼]의 값의 종류를 x, 값의 갯수를 y로 하여 차트화.

### heatmap
```python
sns.heatmap(data=df.corr(numeric_only=True), annot=True, vmin=-1, vmax=1, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.show()
```
- df.corr은 컬럼의 상관계수 데이터프레임
- annot=True는 값 표시
- vmin, vmax는 최소최댓값
- cmap은 표의 테마?
- fmt='.2f'는 소수점 2자리까지 표기
- linewidths는 간격 수정