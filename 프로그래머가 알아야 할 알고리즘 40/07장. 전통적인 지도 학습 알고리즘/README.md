# 07장. 전통적인 지도 학습 알고리즘

# 1. 지도 학습 이해하기

- 특성이라는 입력 정보와 타깃 변수라는 출력 정보 사용
- 수학적 공식을 이용해 특성과 타깃 변수가 이루는 복잡한 관계를 표현하는 모델 훈련

## 1. 지도 학습 구조 소개

- 타깃 변수(Target Variable) : 모델을 통해 예측하고 싶은 변수
- 라벨(Label) : 예측하려는 변수가 카테고리형 변수일 때
- 특성(Feature) : 라벨을 예측하는 데 사용하는 입력 변수
- 특성 엔지니어링(Feature Engineering) : 선택한 지도 학습 알고리즘을 위해 특성들을 변환하는 과정
- 특성 벡터(Feature Vector) : 지도 학습 알고리즘에 데이터를 입력하기 전에 사용할 특성들을 결합해 둔 자료 구조
- 과거 데이터(Historical Data) : 타깃 변수와 특성들의 관계를 학습하기 위해 모은 과거의 데이터
- 훈련/테스트 데이터(Training/Testing Data) : 사례가 담긴 과거 데이터의 두 부분, 훈련 데이터 ≥ 테스트 데이터
- 모델(Model) : 타깃 변수와 특성 간의 관계를 가장 잘 포착한 수학적 공식
- 훈련(Training) : 훈련 데이터로 모델을 학습하는 과정
- 테스트(Testing) : 테스트 데이터로 훈련된 모델의 품질을 평가하는 과정
- 예측(Prediction) : 모델을 이용해 타깃 변수 예측

## 2. 지도 학습의 필요 조건

- 충분히 많은 사례
- 데이터의 패턴
- 유효한 가정

## 3. 분류 모델과 회귀 모델 비교하기

- 분류 모델(Classifier) : 타깃 변수가 카테고리형일 때의 머신러닝 모델
- 회귀 모델(Regressor) : 타깃 변수가 연속형일 때의 머신러닝 모델

# 2. 분류 알고리즘 이해하기

- 라벨이 없는 데이터의 라벨을 예측하여 해당 비즈니스 문제에 대한 답 제공
- 라벨(Label) : 타깃 변수
- 라벨이 있는 데이터(Labeled Data) : 과거 데이터
- 라벨이 없는 데이터(Unlabeled Data) : 예측에 사용할 프로덕션 데이터

## 1. 분류 문제 소개

- 모든 입력 변수들은 전처리를 거쳐 특성 벡터라는 자료 구조로 정리
- 동일한 입력 변수를 사용 → 분류 알고리즘에 따른 성능 비교 가능

### 1. 데이터 파이프라인을 이용한 특성 엔지니어링

- 특성 엔지니어링(Feature Engineering) : 머신러닝 알고리즘에 적합한 형태로 데이터를 준비하는 과정
- 데이터 파이프라인(Data Pipeline) : 여러 단계로 구성된 데이터 처리 코드
- 데이터 읽어오기 : `.csv` 파일 불러오기
- 특성 선별하기(Feature Selection) : 우리가 풀려는 문제의 맥락과 관련한 특성을 선별하는 과정
- 원핫 인코딩하기(One-Hot Encoding) : 카테고리형 변수를 연속형 변수로 변환하는 방법
- 특성과 라벨 설정하기
- 훈련-테스트 분리하기 : 전체 데이터를 훈련 데이터와 테스트 데이터로 8:2(7:3) 분리
    - `X_train` : 훈련 데이터셋의 특성
    - `X_test` : 테스트 데이터셋의 특성
    - `y_train` : 훈련 데이터셋의 라벨
    - `y_test` : 테스트 데이터셋의 라벨
- 특성 스케일링하기 : 특성 표준화(Feature Nomalization), 변수의 스케일을 0과 1로 조정

## 2. 분류 모델 평가하기

- 라벨이 있는 데이터셋을 훈련 데이터셋과 테스트 데이터셋으로 나눔
- 테스트 데이터셋의 특성을 이용해 각 행의 라벨 생성
- 예측 라벨을 실제 라벨과 비교하여 모델 성능 평가

### 1. 혼돈 행렬(Confusion Matrix)

- 분류 모델의 성능 결과 요약
- 참 앙성(True Positive, TP) : 옳게 분류한 양성 예측
- 참 음성(True Negative, TN) : 옳게 분류한 음성 예측
- 거짓 양성(False Positive, FP) : 실제로는 음성이지만 양성으로 예측
- 거짓 음성(False Negative, FN) : 실제로는 양성이지만 음성으로 예측

### 2. 성능 척도

- 정확도(Accuracy) : 전체 예측 중 제대로 예측한 결과의 비율
- 재현률 : 실제 양성인 사례 중에서 양성으로 예측한 사례의 비율
- 정밀도 : 양성으로 예측한 사례 중 실제로 양성인 비율
- F1 점수 : 재현율과 정밀도를 모두 반영한 척도

### 3. 과적합(Overfitting)

- 프로덕션 환경에서 눈에 띄게 부진한 것
- 훈련된 모델이 지나치게 훈련 데이터에 의존적
- 편향 : 특정한 가정들에 기반을 두고 훈련
- 분산 : 모델 훈련에 사용하는 데이터셋이 달라졌을 때 모델이 타깃 변수를 얼마나 정확하게 추정할 수 있을지 정량화한 것
- 편향-분산 상충 관계 : 선택한 알고리즘, 데이터의 특징과 다양한 하이퍼 파라미터에 의해 결정

## 3. 분류 모델 구축 단계

- 모델 훈련, 평가 : 라벨이 있는 데이터 사용
- 배포 : 모델이 라벨이 없는 데이터의 라벨을 예측하여 현실 세계의 문제 해결

## 4. 결정 트리 분류 알고리즘

- 재귀 분할 방식으로 라벨을 예측하는 규칙 생성
- 사람이 이해할 수 있는 라벨 분류 규칙 생성

### 1. 결정 트리 분류 알고리즘 이해하기

- 가장 중요한 특성 찾기 : 정보 획득, 지니 불순도
- 브랜치 나누기 : 해당 특성을 만족하는 데이터 포인트, 해당 특성을 만족하지 않는 데이터 포인트
- 리프 노드 여부 확인하기
- 종료 조건 확인 및 반복하기

### 2. 분류 문제에 결정 트리 분류 알고리즘 적용하기

- 결정 트리 분류 모델 인스턴스 생성, 훈련 데이터 모델 훈련

    ```python
    classifier = sklearn.tree.DecisionTreeClassifier(criterion='entropy', random_state=100, max_depth=2)
    classifier.fit(X_train, y_train)
    ```

- 훈련된 모델을 이용해 테스트 데이터의 라벨 예측

    ```python
    import sklearn.metrics as metrics
    
    y_pred = classifier.predict(X_test)
    cm = metrics.confusion_matrix(y_test, y_pred)
    ```

- 결정 트리의 정확도, 재현율, 정밀도 계산

    ```python
    accuracy = metrics.accuracy_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    print(accuracy, recall, pricision)
    ```


### 3. 결정 트리 분류 모델의 강점과 약점

- 강점
    - 화이트박스 모델 : 사람이 이해하기 쉬운 규칙을 가진 모델
    - 카테고리형 변수가 많은 문제에 잘 동작
- 약점
    - 생성하는 트리가 너무 깊어지면 과적합되기 쉬움
    - 결정 트리가 만들어내는 규칙들은 비선형성을 표현하지 못함

### 4. 활용 사례

- 기록 분류
    - 모기지 서류 심사
    - 고객 세분화
    - 의료 진단
    - 치료 효과 분석
- 특성 선별

## 5. 앙상블 알고리즘

- 여러 파라미터로 복수의 모델을 만든 후 이를 조합한 모델을 생성

### 1. XGBoost 알고리즘으로 그레이디언트 부스팅 구현하기

- 서로 연결된 트리 집단 생성, 경사하강법을 사용하여 잔여 오차 최소화
- 아파치 스카프, 구글 클라우드 플랫폼, 아마존 웹 서비스

    ```python
    from xgboost import XGBClassifier
    
    classifier = XGBClassifier()
    classifier.fit(X_train, y_train)
    
    y_pred = classifier.predict(X_test)
    cm = metrics.confusion_matrix(y_test, y_pred)
    
    accuracy = metrics.accuracy_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    print(accuracy, recall, precision)
    ```


### 2. 랜덤 포레스트 알고리즘 사용하기

- 여러 결정 트리를 묶어 편향과 분산을 낮추는 앙상블 기법
- 랜덤 포레스트 알고리즘으로 생성된 개별 트리들은 서로 독립적임

    ```python
    from sklearn.ensemble import RandomForestClassifier
    
    classifier = RandomForestClassifier(n_estimators=10, max_depth=4, criterion='entropy', random_state=0)
    classifier.fit(X_train, y_train)
    
    y_pred = classifier.predict(X_test)
    cm = metrics.confusion_matrix(y_test, y_pred)
    
    accuracy = metrics.accuracy_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    print(accuracy, recall, precision)
    ```


## 6. 로지스틱 회귀 알고리즘

- 이진 분류에 사용하는 분류 알고리즘
- 로지스틱 함수를 이용해 입력 변수와 타깃 변수 간 상호작용 표현
- 훈련 데이터셋에는 결측치(Missing Value)가 없음
- 라벨은 이진 순서 카테고리형 변수임
- 모든 특성 또는 입력 변수는 서로 독립적임

    ```python
    from sklearn.linear_model import LogisticRegression
    
    classifier = LogisticRegression(random_state=0)
    classifier.fit(X_train, y_train)
    
    y_pred = classifier.predict(X_test)
    cm = metrics.confusion_matrix(y_test, y_pred)
    
    accuracy = metrics.accuracy_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    print(accuracy, recall, precision)
    ```


## 7. 서포트 벡터 머신(Support Vector Machine, SVM) 알고리즘

- 두 클래스 간의 마진을 최대화하는 최적의 초평면을 찾는 분류 모델
- 마진 : 클래스 사이의 결정 경계를 의미하는 초평면과 서포트 벡터라는 초평면에 가장 가까운 훈련 샘플들 사이의 거리

    ```python
    from sklearn.svm import SVC
    
    classifier = SVC(kernel='linear', random_state=0)
    classifier.fit(X_train, y_train)
    
    y_pred = classifier.predict(X_test)
    cm = metrics.confusion_matrix(y_test, y_pred)
    
    accuracy = metrics.accuracy_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    print(accuracy, recall, precision)
    ```


## 8. 나이브 베이즈(Naive Bayes) 알고리즘

- 확률론에 기반을 둔 단순한 알고리즘
- 입력 특성들이 서로 독립적이라는 나이브한 가정 사용
- 베이즈 정리 사용
- 독립적(Independent) 사건 : 다른 사건의 확률에 영향을 미치지 않음
- 의존적(Dependent) 사건 : 다른 사건의 확률에 영향을 미침
- 상호 배타적(Mutually Exclusive) 사건 : 동시에 일어날 수 없음

### 1. 베이즈 정리 이해하기

- 두 독립 사건의 조건부 확률을 계산하는 데 사용

### 2. 확률 계산하기

- 단일 사건이 발생할 확률은 해당 사건의 발생 빈도를 해당 사건으로 이어질 가능성이 있는 프로세스의 전체 개수로 나누어 구함

### 3. AND 사건과 곱셈 법칙

- 두 사건이 독립적 → 간단한 곱셈 법칙으로 각 사건이 동시에 발생할 확률 구함

### 4. 일반적인 곱셈 법칙

- 두 개 이상의 사건들이 독립적이 아님 → 두 사건이 형성하는 의존 관계 반영

### 5. OR 사건과 덧셈 법칙

- 상호 배타적인 두 사건 중 하나가 발생할 확률 계산

### 6. 분류 문제에 나이브 베이즈 적용하기

```python
from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
cm = metrics.confusion_matrix(y_test, y_pred)

accuracy = metrics.accuracy_score(y_test, y_pred)
recall = metrics.recall_score(y_test, y_pred)
precision = metrics.precision_score(y_test, y_pred)
print(accuracy, recall, precision)
```

## 9. 분류 알고리즘 비교하기

- 결정 트리 : 정확도, 재현율 우수
- SVM, 나이브 베이즈 : 정밀도 우수