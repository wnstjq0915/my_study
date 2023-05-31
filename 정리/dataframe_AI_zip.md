# 인공지능

## Regression 회귀분석
- x값을 넣었을 때 y를 예측해줌.

### 작동방식
- 산점도를 그렸을 때, 각 점들과의 거리의 합이 최소가 되는 그래프를 그림.

### 코드
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ex
# 1. X와 y 나누기
y = df['Car Purchase Amount']
X = df.loc[ : , 'Gender' : 'Net Worth']

# 2. 학습시킬 데이터와 테스트할 데이터를 나누기
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=50)

# 3. 학습시키기
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
# regressor.fit(X_train.values, y_train.values)

# 4. 예측한 값과 실제값을 비교하기
y_pred = regressor.predict(X_test)
((y_test - y_pred) **2).mean()

# 5. X가 아닌 다른 값으로 예측해보기.
new_data = np.array([1, 50, 40000, 50000, 200000])
new_data = new_data.reshape(1, 5) # 오류를 막기 위해 차원 변경.
regressor.predict(new_data)

# 6. 학습된 인공지능 파일 생성
import joblib
joblib.dump(regressor, 'regressor.pkl')
# (인공지능 변수, 파일명)
```
#### 1
- X, y를 정하는데 두 데이터의 차원이 다르므로 대소문자로 구분
- .loc를 통해 슬라이싱으로 행과 열을 가져옴.
#### 2
- 학습시킬값1, 테스트할 값1, 학습시킬값2, 테스트값2 순으로 변수 선언
- test_size는 데이터를 나눌 비율. 0.8은 학습데이터로, 0.2는 테스트데이터로 나눔.
- random_state는 학습데이터와 테스트데이터를 랜덤하게 나누기 위해 사용
#### 3
- 데이터가 담겨있지 않은 인공지능을 리그레서라는 변수로 선언
- fit을 통해 X와 y의 학습데이터로 학습. 두 데이터의 관계를 학습함.
- 이와 같은 경우엔 X와 y의 인덱스나 컬럼에 의해서 예측할 때마다 warning이 뜨는데 학습시킬 때 regressor.fit(X_train.values, y_train.values)를 통해 방지가능.
#### 4
- 학습된 regressor에 .predict(X_test)를 통해 X를 넣었을 때의 예측값을 변수 y_pred에 할당.
- 예측한 값(y_pred)과 실제값(y_test)의 값의 차이를 양수로 변환해 평균을 냄. 이를 통해 정확도 판단.
#### 5
- X의 컬럼 갯수에 맞게 데이터 생성
- 차원을 맞추기 위해 reshape
- 생성한 데이터로 예측

## K-Means 군집(clustering)
- 데이터를 분류함.

### 용어
- 클러스터: 어떠한 요소들을 묶은 단위체
- 센트로이드: 클러스터의 평균(중심)
- 이너셔: 센트로이드와 클러스터에 속한 샘플과의 거리의 제곱 합을 이너셔라 함.

### 작동방식
- 1. 무작위로 k개의 클러스터 중심을 정함
- 2. 각 샘플에서 가장 가까운 클러스터 중심을 찾아 해당 클러스터 샘플로 지정.
- 3. 클러스터에 속한 샘플의 평균값으로 클러스터 중심 변경
- 4. 클러스터 중심에 변화가 없을 때까지 2번으로 돌아감.  
(클러스터 중심의 위치가 바뀌면 다시 2번부터.)

### 클러스터의 갯수 정하기
- 엘보우
- 일반적으로 클러스터의 갯수가 늘어나면 이너셔가 감소하는데, 클러스터 - 이너셔 그래프에서 보면 감소하는 속도가 꺾이는 지점이 있다. 그 지점을 k

### 데이터 전처리
- K-Means를 하기 전에 문자열 데이터를 처리하기 위해 밑과 같은 코드를 사용.
- 문자열값의 종류가 2개라면 레이블 인코딩, 3개 이상이면 원핫 인코딩 사용.
- 분석할 데이터 X의 컬럼값을 하나하나 for문을 돌리며 X_new 변수에 새로 담음.

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

X_new = pd.DataFrame()
for name in X.columns: # 각 컬럼을 name으로 받아서 반복
    if X[name].dtype == object: # 문자열로 이뤄졌을 경우 데이터 종류 수 확인
        if X[name].nunique() >= 3: # 원핫 인코딩
            ct = ColumnTransformer([('encoder', OneHotEncoder(), [0])], 
                                    remainder= 'passthrough')
            col_names = sorted(X[name].unique())
            X_new[col_names] = ct.fit_transform( X[name].to_frame())

        else: # 레이블 인코딩
            label_encoder = LabelEncoder()
            X_new[name] = label_encoder.fit_transform(X[name])

    # 숫자 데이터일 때 처리는 여기서
    else:
        X_new[name] = X[name]
```
#### 원핫인코딩
- 3개의 열을 받았을 때로 가정.
- ct 변수는 0열을 원핫인코딩하는 코드이며, remainder의 기본값인 drop은 변환한 열 이외의 남은 두 열을 삭제함. 'passthrough'로 설정하면 열을 삭제하지 않음.
- 컬럼값들을 정렬하여 col_names 변수에 할당.
- X_new에 X[name].unique()값을 각각 컬럼으로 할당. 할당하며 원핫인코딩 진행.
#### 레이블 인코딩
- 인코더를 변수에 불러옴.
- 인코딩할 컬럼을 변수.fit_transfrom() 안에 넣어서 인코딩.

### 코드
```python
# 1.
from sklearn.preprocessing import MinMaxScaler, StandardScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform( X )

# 2. 엘보우를 하기 위해 그래프 그릴 준비
from sklearn.cluster import KMeans
wcss = []
for k in range(1, 10+1): # 군집 갯수 1~10의 데이터
    kmeans = KMeans(n_clusters= k, random_state= 5, n_init='auto')
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_) # inertia는 값이 얼마나 모여있는지 수치화

# 3. 그래프 그리기
import numpy as np
x = np.arange(1, 10+1)
plt.plot(x, wcss)

plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('wcss')
plt.show()

# 4. 클러스터를 4개로 정하고 분류한 그룹을 df['Group']을 만들어 각각 할당.
kmeans = KMeans(n_clusters=4, random_state=5, n_init='auto')
y_pred = kmeans.fit_predict(X_scaled)
df['Group'] = y_pred
```
#### 1
- X컬럼의 각 값들을 백분위로 표현.
#### 2
- 클러스터 1 ~ 10의 inertia를 수치화
#### 3
- 클러스터 - inertia 그래프에서 기울기가 크게 바뀌지 않을 때의 값을 클러스터의 갯수로 정하고 k means 사용
