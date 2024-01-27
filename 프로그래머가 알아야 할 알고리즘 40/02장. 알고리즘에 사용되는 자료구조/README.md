# 02장. 알고리즘에 사용되는 자료 구조

# 1. 파이썬 자료 구조 파악하기

- 컬렉션(Collection) : 함께 저장되고 처리되는 데이터 요소들의 묶음
    - 리스트(list) : 순서 존재, 수정 가능한 일련의 요소
    - 튜플(Tuple) : 순서 존재, 수정 불가능한 일련의 요소
    - 세트(Set) : 순서 없는 요소들의 묶음
    - 딕셔너리(Dictionary) : 순서 없는 키-값 쌍의 묶음
    - 데이터프레임(Dataframe) : 이차원 데이터를 저장하기 위한 이차원 구조

## 1. 리스트

- 수정 가능한 일련의 요소들을 저장하는 데 주로 사용
    
    ```python
    aList = ["John", 33, "Toronto}, True]
    print(aList)
    ```
    

### 1. 리스트 사용하기

- 리스트 인덱싱(List Indexing) : 리스트의 특정 위치에 존재하는 요소 접근 가능
    
    ```python
    bin_colors = ['Red', 'Green', 'Blue', 'Yellow']
    bin_colors[인덱스]
    ```
    
- 리스트 슬라이싱(List Slicing) : 인덱스의 범위를 지정하여 리스트의 일부에 접근하는 것
    
    ```python
    bin_colors = ['Red', 'Green', 'Blue', 'Yellow']
    bin_colors[시작 인덱스:끝 인덱스] # 시작 인덱스 포함, 끝 인덱스 미포함
    ```
    
- 네거티브 인덱싱(Negative Indexing) : 리스트의 끝에서부터 거꾸로 셈
    
    ```python
    bin_colors = ['Red', 'Green', 'Blue', 'Yellow']
    bin_colors[:음수 인덱스]
    ```
    
- 내포(Nesting) : 리스트를 리스트 안에 넣음
    
    ```python
    a = [1, 2, [100, 200, 300], 6]
    ```
    
- 반복(Iteration) : for 루프를 통해서 리스트 안에 든 요소 반복적으로 처리 가능
    
    ```python
    bin_colors = ['Red', 'Green', 'Blue', 'Yellow']
    for aColor in bin_colors:
        print(aColor + " Square")
    ```
    

### 2. 람다 함수(Lambda)

- 함수 즉시 생성 가능, 익명 함수(Anonymous Function)
- 데이터 필터링 : 조건 함수 설정, 단일 인수를 입력받아 불 값 반환
    
    ```python
    list(filter(lambda x: x > 100, [-5, 200, 300, -10, 10, 1000]))
    ```
    
- 데이터 변환 : 맵 함수는 람다 함수를 이용해 데이터 변환
    
    ```python
    list(map(lambda x: x ** 2, [11, 22, 33, 44, 55]))
    ```
    
- 데이터 집계 : 리스트를 순회하면서 값 쌍을 재귀적으로 처리, `reduce`
    
    ```python
    from fuctools import reduce
    
    def doSum(x1, x2):
        return x1 + x2
    
    x = reduce(doSum, [100, 122, 33, 4, 5, 6])
    ```
    

### 3. range 함수

- 숫자로 구성된 큰 리스트 쉽게 생성 가능
    
    ```python
    x = range(요소 개수)
    y = range(시작 요소, 끝 요소, 건너뛸 숫자)
    ```
    

### 4. 리스트의 시간 복잡도

- 요소 삽입 : O(1)
- 요소 제거 : O(n), 최악의 경우 전체 리스트 순회
- 리스트 슬라이싱 : O(n)
- 요소 접근 : O(n)
- 복사 : O(n)

## 2. 튜플(Tuple)

- 수정할 수 없는 자료구조, 읽기만 가능 → 처리 속도 향상

### 1. 튜플의 시간 복잡도

- 요소 추가 : O(1)

## 3. 딕셔너리(Dictionary)

- 키-값 쌍이 저장되는 자료구조
    
    ```python
    bin_colors = {
        "manual_color":"Yellow",
        "approved_color":"Green",
        "refused_color":"Red"
    }
    ```
    

### 1. 접근 및 갱신

- 접근 : 키를 사용해 값에 접근
    
    ```python
    bin_colors.get('approved_color')
    bin_colors['approved_color']
    ```
    
- 갱신 : 키에 대응하는 값 갱신
    
    ```python
    bin_colors['approved_color'] = "Purple"
    ```
    

### 2. 딕셔너리의 시간 복잡도

- 키 또는 값에 접근 : O(1)
- 키 또는 값을 설정 : O(1)
- 딕셔너리 복사 : O(n)