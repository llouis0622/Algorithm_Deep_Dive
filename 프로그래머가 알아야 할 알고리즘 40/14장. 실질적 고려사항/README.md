# 14장. 실질적 고려사항

# 1. 실질적 고려사항 살펴보기

- 알고리즘으로 문제를 해결하는 방식 자체에 관한 현실적인 측면 고려
- 알고리즘을 문제에 실제로 적용하는 과정에서 관련한 규제 정책 이해 필요

## 1. AI 트위터 봇의 슬픈 사연

- 잘못된 데이터로 학습한 Tay는 스스로 문제가 될 만한 트윗 작성
- 알고리즘이 새로운 정보를 즉석으로 학습할 때 발생할 수 있는 전형적인 실패 사례

# 2. 알고리즘의 해석 가능성(Explainability) 이해하기

- 블랙박스 알고리즘 : 작동 원리가 너무 복잡하여 사람이 이해할 수 없는 알고리즘
- 화이트박스 알고리즘 : 사람이 로직을 이해할 수 있는 알고리즘
- 해석 가능성 : 어떤 알고리즘이 왜 특정한 결과를 출력했는지 사람이 이해할 수 있다는 개념

## 1. 머신러닝 알고리즘과 해석 가능성

- 머신러닝 모델이 출력하는 결과를 바탕으로 의사결정 → 사용자가 모델을 신뢰할 수 있어야 함

### 1. 해석 가능성 전략

- 전역적 해석 가능성 전략 : 모델 전체의 작동 방식에 대한 구체적인 내용 제공
    - 개념 활성화 벡터 테스팅(Testing with Concept Activation Vector, TCAV) : 사용자가 정의한 개념과 이미지 라벨 사이의 관계를 정량화하는 방향 미분 계수 활용
    - 부분 의존 플룻(Parital Dependence Plot)
    - 순열 중요도(Permutation Importance)
- 국소적 해석 가능성 전략 : 모델의 개별적인 예측 결과에 대한 근거 제공

### 2. 해석 가능성 구현하기

- 모델 무관 국소적 해석 기법(Local Interpretable Model-Agnostic Explanations, LIME) : 대상 모델의 종류나 특성에 관계없이 개별 예측 결과 설명
- 모델에 전달하는 입력 데이터를 조금씩 변형시켰을 때 국소적 결정 경계에 어떤 영향을 미치는지 파악하는 방식

    ```python
    import sklearn as sk
    import numpy as np
    from lime.lime_tabular import LineTabularExplainer as ex
    
    pkl_file = open('housing.pkl', 'rb')
    housing = pickle.load(pkl_file)
    pkl_file.close()
    housing['feature_names']
    
    from sklearn.ensemble import RandomForestRegressor
    
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_split(housing_data, housing.target)
    
    regressor = RandomForestRegressor()
    regressor.fit(X_train, y_train)
    
    cat_col = [i for i, col in enumerate(housing.data.T) if np.unique(col).size < 10]
    
    myexplainer = ex(X_train, feature_names=housing.feature_names, class_names=['price'], categorical_features=cat_col, mode='regression')
    
    from matplotlib import pyplot as plt
    
    plt.tight_layout()
    
    for i in [1, 35]:
        exp = myexplainer.explain_instance(X_test[i], regressor.predict, num_features=10)
        exp.as_pyplot_figure()
        plt.tight_layout()
    ```

- 예측에 사용된 변수들은 플롯의 y축에 표기
- 각 변수의 중요도는 막대 길이와 비례
- 붉은 막대는 해당 변수가 예측 결과에 부정적인 영향을 미침
- 초록 막대는 긍정적인 영향을 미침

# 3. 알고리즘의 윤리 이해하기

- 알고리즘을 통한 패턴 분류 → 직접 또는 간접적으로 윤리에 반하는 의사결정 초래 가능성 존재

## 1. 학습 알고리즘(Learning Algorithm)이 가진 문제

- 알고리즘에 데이터를 실시간으로 입력하여 끊임없이 새로운 패턴 학습 가능
- 환경 변화에 유연하게 대응 가능
- 윤리 문제가 있는 추론 가능성도 존재

## 2. 윤리적 고려사항 이해하기

- 사회 문제에 분류 알고리즘을 적용하여 개인 또는 집단에 영향을 주는 경우
- 직업 알선에 추천 엔진을 사용하는 경우
- 개인의 데이터를 수집하여 정부의 의사결정에 사용하는 경우
- 외국인 대상 비자 발급에 머신러닝 알고리즘을 사용하는 경우

### 1. 불완전한 증거

- 머신러닝 알고리즘을 학습하는 데 사용하는 데이터 → 불완전할 수 있음
- 바탕이 되는 데이터가 온전한지 확인 필요
- Garbage-In, Garbage-Out

### 2. 추적 가능성

- 머신러닝 알고리즘에 투입되는 훈련 데이터와 테스트 데이터가 서로 다른 특징을 갖는 경우 문제가 발생했을 때 원인을 추적하기 어려움
- 추론 결과를 통해 내린 의사결정이 어떤 대상에게 영향을 미쳤는지 파악하기 어려움

### 3. 불공정한 결론

- 사회적 약자나 그 집단에 불리한 결과를 초래할 수 있음
- 고급 데이터와 정교한 수학 모델 사용 → 알고리즘의 결론이 불공정 → 전체적으로 실이 큼

# 4. 모델의 편향 줄이기

- 사람들이 가진 편향은 알고리즘이 사용하는 데이터나 알고리즘 그 자체에 반영
- 라벨이 없는 데이터 수집
- 수집한 데이터에 라벨 부여
- 모델 훈련
- 평가, 배포

# 5. NP-난해 문제 다루기

## 1. 문제를 단순화하기

- 가정을 이용해 문제를 단순화
- 완벽하지는 않아도 충분히 잘 동작하며 통찰력있는 결과를 만들어 낼 수 있음
- 사용하는 가정들이 가급적 비제한적이어야 함
- 선형적 관계 가정 → 알고리즘을 단순화하고 활용성 증가 가능

## 2. 널리 알려진 다른 해결책을 수정해 사용하기

- 비슷한 문제에 이미 해결책이 존재하는 경우 그 해결책을 시작점으로 삼을 수 있음
- 전이 학습 : 이미 훈련이 끝난 모델을 이용해 또 다른 알고리즘 학습의 시작점으로 설정
- 사물 인식 작업

## 3. 확률적 모델 사용하기

- 문제를 푸는 최적의 해결책은 아니지만 어느 정도 좋은 결과 획득 가능
- 결정 트리 알고리즘
- 주어진 제약 조건 하에서 문제를 푸는 유용한 방법
- 매우 복잡한 문제를 정해진 시간 내에 풀어야 할 때 사용

# 6. 알고리즘을 사용해야 할 때

- 비용 : 알고리즘을 구현하고 개발하는 데 드는 비용을 감당할 수 있는가
- 시간 : 새로운 해결책이 기존 방식에 비해 프로세스의 효율을 개선하는가
- 정확도 : 새로운 해결책이 기존 방식에 비해 더 정확한 결과를 만들어내는가
- 가정을 사용해서 문제를 단순화할 수 있는가
- 알고리즘을 어떻게 평가할 수 있는가
- 주요 지표는 무엇인가
- 어떻게 배포하고 사용할 것인가
- 해석 가능해야 하는가
- 보안, 성능, 가용성 요구조건을 이해하고 있는가
- 데드라인이 존재하는가