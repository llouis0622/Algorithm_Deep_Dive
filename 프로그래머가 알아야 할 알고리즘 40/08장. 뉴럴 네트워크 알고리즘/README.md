# 08장. 뉴럴 네트워크 알고리즘

# 1. 뉴럴 네트워크(Artificial Neural Network, ANN) 이해하기

- 인간의 두뇌 속 뉴런에 영감
- 퍼셉트론(Perceptron) : 은닉층이 없는 간단한 뉴럴 네트워크, 선형 회귀 모델과 비슷
    - 각 입력 신호에 해당하는 가중치를 곱한 후 모두 더함
    - 가중합의 결과에 따라 참 또는 거짓을 출력하는 이진 분류기
    - 탐색하려는 신호가 입력 데이터에서 발견되면 퍼셉트론은 참 신호 발생

# 2. 뉴럴 네트워크의 발전 살펴보기

- 퍼셉트론은 복잡한 로직을 학습할 수 없음
- XOR과 같은 단순한 로직 함수도 학습하기 어려움
- AI 겨울 : 뉴럴 네트워크에 대한 세간의 관짐 떨어짐, 암흑기
- AI 봄 : 분산 컴퓨팅 기술 발전 및 인프라 보급
- 다층 퍼셉트론(Multilayer Perceptron) : 여러 층으로 구성된 뉴럴 네트워크
    - 입력층(Input Layer)
    - 은닉층(Hidden Layer)
    - 출력층(Output Layer)
- 뉴런 : 네트워크를 구성하는 기본 단위, 한 층에 속한 뉴런들은 다음 층의 모든 뉴런들에 연결

# 3. 뉴럴 네트워크 훈련하기

- 연산을 통해 최적의 가중치 값을 구하는 것

## 1. 뉴럴 네트워크 구조

- 층(Layer) : 뉴럴 네트워크를 구성하는 핵심 요소
    - 하나 이상의 입력 데이터를 어떤 형태로 가공하여 하나 이상의 출력 데이터를 만들어냄
    - 데이터가 층 하나를 통과할 때마다 뉴럴 네트워크는 질문과 연관된 패턴을 찾으려 노력
- 손실 함수(Loss Function) : 학습 프로세스에서 피드백 신호 제공, 하나의 샘플이 정답에서 얼마나 멀어졌는지 알려 주는 역할 수행
- 비용 함수(Cost Function) : 전체 샘플에 대한 손실 함수
- 옵티마이저(Optimizer) : 손실 함수에서 얻은 피드백 시그널을 어떻게 해석할지 결정
- 입력 데이터(Input Data) : 뉴럴 네트워크를 훈련하는 데 쓰는 데이터
- 가중치(Weight) : 각 입력 정보를 그 중요성에 맞게 조절하는 역할
- 활성화 함수(Activation Fuction) : 입력 정보를 가중치와 곱하고 나서 집계하는 것

## 2. 경사하강법

- 초기에 무작위로 설정된 가중치를 반복 수정하여 최적화
- 가중치는 비용을 최소화하는 방향으로 수정
    - 방향(Direction) : 손실 함수의 최저점에 도달하기 위해 어떤 방향으로 이동할 것인가?
    - 학습률(Learning Rate) : 선택한 방향으로 얼마나 멀리 이동할 것인가?
- 역전파(Backpropagation) : 마지막 층의 기울기를 먼저 계산하고 그 다음 층 처리

## 3. 활성화 함수

- 뉴런에 전달된 입력 정보를 처리해 출력하는 방식
- 적절한 활성화 함수 선택 중요

### 1. 임계 함수(Threshold Function)

- 이진, 0 또는 1
- 활성화 함수의 입력값이 0보다 크면 1 출력

### 2. 시그모이드 함수(Sigmoid Fuction)

- 임계 함수의 단점 보완
- 활성화 함수의 민감도 조절 가능
- 0과 1 사이의 실수로 출력

### 3. ReLU 함수

- 입력 변수를 연속적인 단일 출력값으로 변환
- 변수의 연속성을 유지하려는 은닉층에 사용
- 입력 정보 중 0보다 작은 값은 모두 0으로 변환

### 4. Leaky ReLU 함수

- ReLU 함수의 단점 보완
- ß 값 임의 설정
- ß 값 뉴럴 네트워크의 파라미터로 설정하여 훈련을 통해 적절한 값 학습, 파라메트릭 ReLU(Parametric ReLU)
- ß 값 무작위 설정, 무작위 ReLU(Randomized ReLU)

### 5. Tanh 함수

- 시그모이드 함수와 비슷
- 신호를 음수로 출력 가능

### 6. 소프트맥스 함수

- 다중 클래스 분류 문제에 적합
- 각 클래스별 예측 확률 출력

# 4. 도구와 프레임워크 살펴보기

## 1. 케라스(Keras)

- 손쉽게 뉴럴 네트워크를 만들 수 있음
- 기획 단계부터 쉽고 빠른 딥러닝 구현 염두
- 하이레벨 블록만 지원

### 1. 케라스의 백엔드 엔진

- 로우레벨 딥러닝 라이브러리
- 텐서 차원의 조작 수행
- 텐서플로
- Theano
- Microsoft Cognitive Toolkit(CNTK)

### 2. 딥러닝 기술 스택의 로우레벨 레이저

- CPU : Eigen, 로우레벨 텐서 연산 라이브러리
- GPU : cuDNN(CUDA Deep Neural Network), 엔비디아 라이브러리

### 3. 하이퍼 파라미터

- 활성화 함수
- 학습률
- 은닉층의 개수
- 각 은닉층의 뉴런 개수

### 4. 케라스 모델 정의하기

- 사용할 층 정의
  - 순차형 API(Sequential)
  - 함수형 API(Fuctional)

    ```python
    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras import Input
    from tensorflow.keras.layers import Flatten, Dense, Activation, Dropout
    from tensorflow.keras.datasets import mnist
    
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    
    model = Sequential([
        Flatten(input_shape=(128, 128)),
        Dense(128, activation='relu'),
        Dropout(0.2),
        Dense(10)
    ])
    
    inputs = Input(shape=(128, 128))
    x = Flatten()(inputs)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.2)(x)
    x = Dense(10)(x)
    model = tf.keras.Model(inputs=inputs, outputs=x)
    ```

- 학습 프로세스 정의
  - 옵티마이저
  - 손실 함수
  - 모델의 성능을 정량적으로 측정할 수 있는 평가 척도

    ```python
    optimizer = tf.keras.optimizers.Adam(0.001)
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    model.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])
    ```

- 훈련

    ```python
    model.fit(x_train, y_train, batch_size=128, epochs=10)
    ```

- 테스트 데이터를 사용해 모델의 정확도 측정

    ```python
    model.evaluate(x_test, y_test, batch_size=128)
    ```


### 5. 순차형 또는 함수형 모델 선택하기

- 각 층은 단 하나의 입력과 출력 텐서에만 연결
- 모델 안에 있는 어떤 층이 2개 이상의 다른 층에 동시에 연결 → 함수형 모델 사용

## 2. 텐서플로(Tensorflow) 사용하기

- 가장 인기 있는 뉴럴 네트워크 라이브러리
- 수행하려는 연산을 방향성 그래프(Directed Graph, DG)로 표현
  - 연산 작업, 변수, 상수를 표현하는 노드 구성

### 1. 텐서플로의 기본 콘셉트

- 스칼라(Scalar) : 간단한 숫자
- 벡터(Vector) : 크기와 방향을 가진 무엇
- 메트릭스(Matrix) : 2차원 배열
- 3D 텐서(Tensor) : 3차원 배열
- 랭크(Rank) : 자료 구조의 차원을 표현

    ```python
    print('Define constant tensors')
    a = tf.constant(2)
    print('a = %i' %a)
    b = tf.constant(3)
    print('b = %i' %b)
    
    print('Running operations, without tf.Session')
    c = a + b
    print('a + b = %i' %c)
    d = a * b
    print('a * b = %i' %d)
    
    c = a + b
    print('a + b = %s' %c)
    
    d = tf.matmul(a, b)
    print('a * b = %s' %d)
    ```


## 3. 뉴럴 네트워크의 종류

### 1. 컨볼루션 뉴럴 네트워크(CNN, Convolution Neural Network)

- 합성곱 신경망
- 멀티미디어 데이터를 처리하는 데 사용
- 컨볼루션 : 필터 또는 커널이라 부르는 작은 이미지를 이용해 대상 이미지에 담긴 특정한 패턴 증폭
- 풀링 : 다운샘플링, 문제의 전반적인 차원을 줄여서 모델을 학습하는 대 드는 시간 단축
- 맥스 풀링 : 각 블록에서 최댓값을 선택한 것
- 에버리지 풀링 : 각 블록에서 평균값을 선택한 것

### 2. 리커런트 뉴럴 네트워크(Recurrent Neural Network, RNN)

- 반복적인 구조를 가진 뉴럴 네트워크
- 메모리 보유 → 최근에 처리한 정보 저장 가능

### 3. 적대적 생성 네트워크(Generative Adversarial Network, GAN)

- 세상에 존재하지 않는 데이터를 만들어내는 뉴럴 네트워크의 한 종류
- 합성 데이터로 훈련에 사용할 데이터셋을 확충하는 데 사용

# 5. 전이 학습 이해하기(Transfer Learning)

- 매번 대량의 데이터를 모으고 모델을 처음부터 학습시키는 대신에 이미 학습된 모델들을 이용해 학습 가능
- 동영상에서 사물 인식하기
- 이미지에서 사물 인식하기
- 오디오를 텍스트로 변환하기
- 텍스트의 감정 분석하기
- 모델 훈련에 드는 노력 감소 가능
- 검증되고 안정적인 성능을 자랑하는 모델 사용 → 전반적인 모델의 퀄리티 개선 가능성 증가
- 데이터가 충분하지 않을 때 미리 학습된 모델을 이용 가능