# 13장. 대규모 알고리즘

# 1. 대규모 알고리즘 살펴보기

## 1. 대규모 알고리즘 정의

- 주어진 자원을 최적으로 활용하여 대량의 데이터를 처리하고 요구조건을 만족시킴
- 확장 용이 → 풀려는 문제가 더 복잡해지더라도 자원을 더 추가하는 것만으로 대응 가능

## 2. 기본 용어

- 지연 시간(Latency) : 단일 연산을 수행하는 데 처음부터 끝까지 소요된 시간
- 처리율(Throughput) : 동시에 처리될 수 있는 단일 연산의 개수
- 네트워크 이분 대역폭(Network Bisection Bandwith) : 네트워크 내 동일한 두 부분 사이의 대역폭
- 탄력성(Elasticity) : 처리 요구사항이 갑작스럽게 증가하더라도 자원을 더 할당하여 대응할 수 있는 능력

# 2. 병렬 알고리즘 설계 이해하기

## 1. 암달의 법칙

- 어떤 컴퓨팅 공정이 가진 모든 프로세스를 동시에 실행할 수 없다는 것을 전제로 함
- 컴퓨팅 공정에는 병렬화가 불가능한 순차적인 부분 존재
- 디렉터리에서 파일들을 스캔하고 입력 파일에 부합하는 파일 목록 제작
- 파일들을 읽어들이고, 데이터 파이프라인을 만들고, 파일들을 처리하고, 모델을 훈련함

## 2. 작업 세분성(Task Granularity)

- 병렬 작업 개수가 너무 적다면 병렬 컴퓨팅의 호과가 크지 않음
- 작업 개수가 너무 많아지면 부대 비용이 너무 커짐

## 3. 부하 분산(Load Balancing)

- 병렬 컴퓨팅에서 스케줄러는 작업을 실행하는 데 필요한 자원 선택

## 4. 국지성 이슈

- 병렬 컴퓨팅에서 데이터 이동은 가급적 피해야 함
- 가능하다면 데이터를 이동하는 대신, 데이터가 위치한 노드 내에서 처리해야 함

## 5. 파이썬에서 병렬 프로세싱 실행하기

- 대상 프로세스를 복제하여 자식 프로세스를 생성

# 3. 멀티 자원 프로세싱 전략 이해하기

- 내부 방법(Look Within) : 컴퓨터에 내재된 리소스 활용, 대규모 알고리즘을 실행하기 위해 GPU가 가진 수백 개의 코어 사용
- 외부 방법(Look Outside) : 주어진 대규모 문제를 풀기 위해 더 많은 컴퓨팅 자원 이용할 수 있는 분산 컴퓨팅 사용
- 혼합 방법(Hybrid Strategy) : 분산 컴퓨팅을 사용하면서 각 노드에서 GPU 또는 GPU 배열을 이용해 알고리즘 실행

## 1. 컴퓨팅 통합 장치 아키텍처

- CPU는 코어 수가 비교적 적지만 GPU는 수천 개의 코어를 가지고 있음
- GPU는 수천 개의 ALU를 가지고 있으므로 수천 개의 프로세스를 동시에 실행 가능
- CUDA : CPU와 GPU를 각각 호스트와 장치로 추상화
    - 보통 리눅스 커널의 지원과 함께 시작
    - 프로그래밍 언어 API와 CUDA 드라이버 사이를 잇는 역할

### 1. CUDA로 병렬 알고리즘 설계하기

- 비트코인 마이닝
- 대규모 시뮬레이션
- DNA 분석
- 동영상 및 사진 분석
- 단일 프로그램 다수 데이터(Single Program Multiple Data, SPMD)에 부적합

### 2. 파이썬으로 GPU에서 데이터 처리하기

```python
import numpy as np
import cupy as cp
import time

start_time = time.time()
myvar_cpu = np.ones((800, 800, 800))
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
myvar_gpu = cp.ones((800, 800, 800))
cp.cuda.Stream.null.synchronize()
end_time = time.time()
print(end_time - start_time)
```

## 2. 클러스터 컴퓨팅

- 대규모 알고리즘을 위해 구현된 병렬 프로세싱 방법 중 하나
- 다수의 노드를 고속의 네트워크로 서로 연결
- 각 잡은 여러 개의 작업으로 구성, 각 작업은 개별 노드에서 실행
- 아파치 스파크 : 데이터를 탄력적 분산 데이터셋이라 부르는 장애를 견뎌낼 수 있도록 분산된 데이터셋으로 변환
    - 병렬로 처리될 수 있는 요소들의 불변 모음
    - 파티션으로 분리되어 여러 노드에 분산 저장

### 1. 아파치 스파크에서 데이터 프로세싱 구현하기

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('cloudanum').getOrCreate()
df = spark.read.csv('taxi2.csv', inferSchema=True, header=True)

df.columns

df.createOrReplaceTempView('main')

data=spark.sql('SELECT payment_type, Count(*) AS COUNT, AVG(fare_amount), AVG(tip_amount) AS AverageFare from main GROUP BY payment_type')
data.show()
```

## 3. 혼합 방법

- 클라우드 컴퓨팅 : 외부 방법 + 내부 방법 하나로 합침
- 여러 대의 가상 머신에 하나 이상의 GPU 설치
- 데이터를 다수의 파티션으로 분할
- 잘게 쪼갠 데이터를 각 노드에 위치한 GPU에 보내 연산량이 큰 작업을 처리