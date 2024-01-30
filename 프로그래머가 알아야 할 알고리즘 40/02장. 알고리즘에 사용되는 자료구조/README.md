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

## 4. 세트(Set)

- 여러 유형으로 구성된 요소의 컬렉션으로 정의 가능, 요소의 중복 허용하지 않음
    
    ```python
    green = {'grass, 'leaves'}
    ```
    

### 1. 세트 연산

- 벤 다이어그램 연산 가능
    
    ```python
    yellow = {'dandelions', 'fire hydrant', 'leaves'}
    red = {'fire hydrant', 'blood', 'rose', 'leaves'}
    yellow | red # 합집합(Union)
    yellow & red # 교집합(Intersection)
    ```
    

### 2. 세트의 시간 복잡도

- 요소 추가 : O(1)
- 요소 제거 : O(1)
- 복사 : O(n)

## 5. 데이터프레임(Dataframe)

- pandas 라이브러리에서 제공하는 자료구조
- 테이블형 데이터를 저장하는 데 사용, 정형 데이터 처리
    
    ```python
    import pandas as pd
    
    df = pd.DataFrame([
        ['1', 'Fares', 32, True],
        ['2', 'Elena', 23, False],
        ['3', 'Steven', 40, True]])
    df.columns = ['id', 'name', 'age', 'decision']
    ```
    

### 1. 데이터프레임 용어

- 축(Axis) : 데이터프레임의 개별 열(Column)이나 행(Row)
- 축들(Axes) : 둘 이상의 축을 묶은 것
- 라벨(Label) : 열과 행에 이름을 지은 것

### 2. 데이터프레임의 부분 집합 생성하기

- 열 선택 : 열의 순서는 수정하지 않는 한 고정됨 → 인덱스 활용
    
    ```python
    df[['name', 'age']]
    
    df.iloc[:, 3]
    ```
    
- 행 선택 : 각 행은 각 데이터 포인트에 대응 → 인덱스, 필터 사용
    
    ```python
    df.iloc[1:3, :] # 인덱스 사용
    df[df.age>30] # 필터 사용
    ```
    

## 6. 행렬(Matrix)

- 고정된 수의 열과 행을 가진 2차원 자료구조
    
    ```python
    myMatrix = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
    ```
    

### 1. 행렬 연산

- 전치(Transpose) : 열과 행 뒤바꿈
    
    ```python
    myMatrix.transpose()
    ```
    

# 2. 추상화 자료 유형 파악하기

- 추상화(Abstraction) : 공통적인 핵심 함수를 사용해 복잡한 시스템을 정의
- 추상화 자료 유형(Abstract Data Type, ADT) : 일반적인 자료구조에 추상화 개념 적용
    - 사용자가 일반적인 인터페이스 사용 가능
    - 더 깔끔하고 단순한 코드로 알고리즘 구현 가능

## 1. 벡터(Vector)

- 데이터를 저장하는 일차원 자료구조
- 파이썬의 리스트 사용하기 : 리스트형
    
    ```python
    myVector = [22, 33, 44, 55]
    ```
    
- numpy 배열 사용하기 : ndarray형
    
    ```python
    myVector = np.array([22, 33, 44, 55])
    ```
    

## 2. 스택(Stack)

- 일차원 리스트를 저장하는 선형 자료구조
- 후입선출(Last-In First-Out, LIFO), 선입후출(First-In Last-Out, FILO)
- 요소가 추가되거나 제거되는 방식으로 규정
- `isEmpty` : 스택이 비어있으면 True 반환
- `push` : 새 요소를 스택에 추가
- `pop` : 최근에 추가한 요소를 스택에서 제거하고 반환
    
    ```python
    class Stack:
        def __init__(self):
            self.items = []
    
        def isEmpty(self):
            return self.items == []
    
        def push(self, item):
            self.items.append(item)
    
        def pop(self):
            return self.items.pop()
    
        def peek(self):
            return self.items[len(self.items)-1]
    
        def size(self):
            return len(self.items)
    
    stack = Stack()
    
    stack.push('Red')
    stack.push('Green')
    stack.push('Blue')
    stack.push('Yellow')
    
    stack.pop()
    
    stack.isEmpty()
    ```
    

### 1. 스택의 시간 복잡도

- `push` : O(1)
- `pop` : O(1)
- `size` : O(1)
- `peek` : O(1)

## 3. 큐(Queue)

- n개의 요소를 저장하는 일차원 자료구조
- 선입선출(First-In First-Out, FIFO)
- 뒤(Rear) : 큐의 한쪽 끝
- 앞(Front) : 다른 한쪽 끝
- `dequeue` : 요소를 앞에서부터 제거
- `enqueue` : 요소를 뒤에서부터 추가
    
    ```python
    class Queue(object):
        def __init__(self):
            self.items = []
    
        def isEmpty(self):
            return self.items == []
    
        def enqueue(self, item):
            self.items.insert(0, item)
    
        def dequeue(self):
            return self.items.pop()
    
        def size(self):
            return len(self.items)
    
    queue = Queue()
    
    queue.enqueue('Red')
    queue.enqueue('Green')
    queue.enqueue('Blue')
    queue.enqueue('Yellow')
    ```
    

## 4. 트리(Tree)

- 계층적 데이터를 저장할 수 있는 자료구조
- 각 트리는 유한한 수의 노드(Node)로 구성
- 루트(Root) : 트리의 시작이 되는 요소
- 브랜치(Branch) : 노드와 노드 사이의 연결선
- 루트 노드 : 부모 노드가 없음
- 노드 레벨 : 루트 노드에서부터 해당 노드까지의 거리, 깊이
- 형제 노드 : 노드의 레벨이 동일하고 부모 노드가 같은 노드
- 부모 노드와 자식 노드 : 노드가 서로 연결되어 있으면서 깊이가 다른 것
- 노드의 차수(Degree) : 해당 노드가 가진 자식 노드의 수
- 트리의 차수 : 트리를 구성하는 모든 노드가 가진 차수 중 최댓값
- 하위 트리(Sub) : 선택한 노드를 루트 노드로 하여 그 자식 노드를 모두 포함
- 리프 노드(Leaf) : 자식 노드가 없는 노드
- 내부 노드(Internal) : 트리에서 루프 노드나 리프 노드가 아닌 나머지 노드

### 1. 트리 유형

- 이진 트리(Binary Tree) : 트리의 차수가 2인 트리
- 정 트리(Full Tree) : 노드의 차수와 트리의 차수 동일
    - 부정 불포화 트리(Non-Full, Non-Perfect Tree)
    - 정 불포화 트리(Full, Non-Perfect Tree)
    - 정 포화 트리(Full, Perfect Tree)
- 포화 트리(Perfect Tree) : 정 트리의 특수 형태, 모든 리프 노드가 동일한 레벨을 가짐
- 순서 트리(Ordered Tree) : 특정한 기준에 맞추어 자식 노드들이 정렬된 트리
