# 03장. 정렬과 검색 알고리즘

# 1. 정렬 알고리즘 이해하기

## 1. 파이썬에서 변수 바꾸기

```python
var1 = 1
var2 = 2
var1, var2 = var2, var1
```

## 2. 버블 정렬(Bubble Sort)

- 가장 간편하지만 속도가 가장 느린 정렬 알고리즘
- 리스트 안에서 가장 큰 값을 반복적으로 옮김

### 1. 버블 정렬의 작동 원리 이해하기

- 패스(Pass) : 리스트의 정렬이 안된 가장 큰 값을 맨 오른쪽으로 보내는 것
- 인접한 두 값 중 왼쪽 값이 더 크면 서로의 값 위치 바꿈
- 리스트에 있는 모든 요소들이 오름차순으로 정렬될 때까지 반복
    
    ```python
    def BubbleSort(list):
        lastElementIndex = len(list) - 1
        for passNo in range(lastElementIndex, 0, -1):
            for idx in range(passNo):
                if list[idx] > list[idx+1]:
                    list[idx], list[idx+1] = list[idx+1], list[idx]
        return list
    ```
    

### 2. 버블 정렬의 성능 분석

- 외부 루프 : 패스
- 내부 루프 : 패스 내에서 가장 높은 값을 오른쪽으로 이동시킬 때까지 값들을 반복적으로 비교하는 과정
- 시간 복잡도 : O(N^2)

## 3. 삽입 정렬(Insertion Sort)

- 자료 구조에서 데이터 포인터를 하나씩 빼내어 올바른 위치에 집어넣는 과정을 반복
- 맨 왼쪽에 위치한 두 데이터 포인터를 서로 비교하고 값의 크기에 따라 정렬 → 범위를 확장하며 비교
    
    ```python
    def InsertionSort(list):
        for i in range(1, len(list)):
            j = i - 1
            element_next = list[i]
            while (list[j] > element_next) and (j >= 0):
                list[j+1] = list[j]
                j = j - 1
            list[j+1] = element_next
        return list
    ```
    
- 메인 루프 : 리스트 전체 순회
- 루프 안에 등장하는 `list[j]` → 현재 요소, `list[i]` → 그 옆에 인접한 다음 요소

### 1. 삽입 정렬의 성능 분석

- 시간 복잡도 : O(N^2)

## 4. 병합 정렬(Merge Sort)

- 성능이 입력 데이터의 정렬 여부와는 관계 없음
- 맵리듀스와 같은 빅데이터 알고리즘처럼 분할 및 정복 전략 사용
- 분리(Splitting) : 데이터를 재귀적으로 둘로 나눔, 나뉜 부분의 크기가 미리 정한 기준보다 작아질 때까지 반복
- 병합(Merge) : 최종 결과를 얻을 때까지 알고리즘이 병합과 처리 반복
    
    ```python
    def MergeSort(list):
        if len(list) > 1:
            mid = len(list) // 2
            left = list[:mid]
            right = list[mid:]
    
            MergeSort(left)
            MergeSort(right)
    
            a = 0
            b = 0
            c = 0
    
            while a < len(left) and b < len(right):
                if left[a] < right[b]:
                    list[c] = left[a]
                    a = a + 1
                else:
                    list[c] = right[b]
                    b = b + 1
                c = c + 1
            while a < len(left):
                list[c] = left[a]
                a = a + 1
                c = c + 1
            while b < len(right):
                list[c] = right[b]
                b = b + 1
                c = c + 1
        return list
    ```