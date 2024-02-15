# 09장. 자연어 처리 알고리즘

# 1. 자연어 처리(Natural Language Processing, NLP) 살펴보기

- 컴퓨터와 사람의 언어 간 상호작용을 표현하고 형식화하는 방법 탐사
- 주제 식별 : 텍스트에 담긴 주제 도출, 주제별 문서 분류
- 감성 분석 : 대상 텍스트에 담긴 감성이 긍정적인지 부정적인지 분류
- 기계 번역 : 특정 언어를 다른 언어로 번역
- 음성 인식 : 음성을 텍스트로 변환
- 주관적 해석 : 질문을 지능적으로 해석하고 가용한 정보를 바탕으로 답 도출
- 개체명 인식 : 텍스트에서 사람 이름, 지명, 사물의 개체 식별
- 가짜 뉴스 탐지 : 텍스트 내용을 바탕으로 가짜 뉴스 여부 판단

## 1. 자연어 처리 용어 이해하기

### 1. 표준화(Normalization)

- 머신러닝 모델 성능을 개선하기 위해 입력 텍스트 데이터에 적용
- 모든 텍스트를 대문자 또는 소문자로 변환
- 구두점 제거
- 숫자 제거

### 2. 코퍼스(Corpus)

- 우리가 풀려는 문제에 사용하는 문서의 집합

### 3. 토큰화(Tokenization)

- 텍스트를 토큰 리스트로 나누는 것
- 단어
- 문장
- 단어 조합
- 문단

### 4. 개체명 인식(Named Entity Recognition, NER)

- 구조가 없는 비정형 데이터에 구조 제공 가능

### 5. 불용어(Stopword)

- 일부 단어는 거의 모든 문서에 등장할 정도로 흔해서 그 어떤 가치 있는 정보를 제공하지 못함

### 6. 감성 분석(Sentiment Analysis)

- 오피니언 마이닝(Opinion Mining)
- 텍스트로부터 긍정 또는 부정적인 감성을 추출하는 프로세스

### 7. 어간 추출과 표제어 추출

- 어간 추출(Stemming) : 각 단어를 그 원형 또는 어간으로 변환하는 과정
- 표제어 추출(Lemmatization) : 단어의 철자가 정확해야 하는 경우 어간 추출 대신 사용

## 2. 자연어 처리 툴킷(Natural Language Toolkit, NLTK)

- 파이썬 언어로 된 NLP 라이브러리
- 모든 도구를 처음부터 만들 필요 없이 NLP 프로세스 빠르게 개발 가능

# 2. 백오브워즈(Bag-of-Words, BoW) 기반 자연어 처리 이해하기

- 입력 텍스트를 토큰으로 된 가방으로 표현하는 것
- 이진(Binary) : 단어가 텍스트 내에 존재하면 1, 아니라면 0
- 횟수(Count) : 단어가 텍스트 내에 등장하는 빈도를 값으로 하는 특성 생성
- 용어 빈도-역문서 빈도(Term Frequency-Inverse Document Frequency, TF-IDF) : 특정 단어가 전체 문서 코퍼스 중 해당 문서에서 얼마나 중요한지에 대한 값 표현

    ```python
    import numpy as np
    import pandas as pd
    
    dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
    dataset.head()
    
    import re
    import nltk
    
    nltk.download('stopwords')
    
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    
    corpus = []
    for i in range(0, 1000):
        review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
        review = review.lower()
        review = review.split()
        ps = PorterStemmer()
        review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        review = ' '.join(review)
        corpus.append(review)
    
    from sklearn.feature_extraction.text import CountVectorizer
    
    cv = CountVectorizer(max_features=1500)
    X = cv.fit_transform(corpus).toarray()
    y = dataset.iloc[:, 1].values
    
    from sklearn.model_selection import train_test_split
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    from sklearn.naive_bayes import GaussianNB
    
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)
    
    y_pred = classifier.predict(X_test)
    
    from sklearn.metrics import confusion_matrix
    
    cm = confusion_matrix(y_test, y_pred)
    ```


# 3. 단어 임베딩(Word Embedding) 살펴보기

- 단어를 밀집 벡터의 형태로 표현할 수 있음
- 각 단어들을 숫자로 된 리스트인 벡터로 표현

## 1. 단어의 이웃

- BoW : 단어가 가진 이웃 관계 정보 제거 → 이웃을 이용한 맥락 사용 불가

## 2. 단어 임베딩의 특징

- 밀집 : 임베딩 벡터의 각 구성 요소는 해당 특성의 양 표현
- 저차원 : 하이퍼 파라미터로 훈련에 앞서 미리 결정
- 도메인 정보 임베딩 : 훈련이 성공적으로 끝나면 임베딩은 해당 도메인에 대한 의미 이해 가능
- 쉬운 일반화 : 웹 임베딩은 일반화된 추상적인 패턴 습득 가능

# 4. 자연어 처리에 리커런트 뉴럴 네트워크 사용하기

- 리커런트 뉴럴 네트워크(RNN, Recurrent Neural Network) : 피드백 루프를 가진 전통적인 순전파 네트워크
- 시퀀스 데이터를 생성하거나 예측하는 데 사용
- 타이핑할 때 다음 단어가 무엇이 될지 예측하기
- 미리 쓰여진 문장의 스타일을 고려하여 다음 단어를 생성하기