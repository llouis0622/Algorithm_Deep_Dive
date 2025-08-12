## 1️⃣ 우선순위 큐

- pop을 할 때 가장 먼저 들어온 원소가 나오는 대신 우선순위가 가장 높은 원소가 나오는 큐
- 원소의 추가 : O(log N)
- 우선순위가 가장 높은 원소 확인 : O(1)
- 우선순위가 가장 높은 원소 제거 : O(log N)

## 2️⃣ 우선순위 큐 풀이 방법

### **우선순위 큐 선택 가능성**

- 작거나 큰 값을 즉시 꺼내야 하는 경우
- 값들이 지속적으로 들어오고, 정렬된 상태로 꺼내야 할 때
- 가중치가 작은 것부터 처리해야 할 때

### **우선순위 큐 문제 판별법**

- 가장 작은/가장 빠른/최대값/최소값 → 정렬된 상태로 꺼내야 함
- 우선순위, 먼저 처리해야 할, 높은 등급 → 우선순위 처리가 중요
- 항상 현재 가장 작은/큰 원소부터 → 힙 자료구조 활용 가능성 ⬆︎
- 지속적인 삽입과 제거 + 정렬 유지 → 큐나 정렬된 리스트보다 힙이 더 효율적

### **우선순위 큐 풀이 기본 흐름**

- 우선순위 기준 파악 – 우선순위를 무엇으로 판단하는지 명확히 파악
- 튜플 구조 설계 – (우선순위, 실제값) 형태로 push
- 힙 자료구조 사용 – heapq, PriorityQueue 등
- 반복적으로 꺼내면서 처리 – 가장 높은/낮은 우선순위부터 처리

## 3️⃣ 수업 코드

### 최소 힙 구현

```python
heap = [0] * 100005
sz = 0

def push(x):
    # heap[sz+1] 자리에 x를 넣고
    # 부모와 비교해서 작으면 swap하며 위로 올림

def top():
    # heap[1] 반환

def pop():
    # heap[1] 자리에 heap[sz]를 옮기고 sz 줄임
    # 자식 중 작은 쪽과 비교해서 필요 시 swap하며 아래로 내림

def test():
    push(10)
    push(2)
    push(5)
    push(9)
    print(top())  # 2
    pop()
    pop()
    print(top())  # 9
    push(5)
    push(15)
    print(top())  # 5
    pop()
    print(top())  # 9

test()
```

```java
public class MinHeap {
    static int[] heap = new int[100005];
    static int sz = 0;

    static void push(int x) {
        // heap[++sz] = x;
        // 부모와 비교해서 작으면 swap하며 위로 올림
    }

    static int top() {
        // return heap[1];
    }

    static void pop() {
        // heap[1] = heap[sz--];
        // 자식 중 작은 쪽과 비교해서 필요 시 swap하며 아래로 내림
    }

    public static void test() {
        push(10);
        push(2);
        push(5);
        push(9);
        System.out.println(top());  // 2
        pop();
        pop();
        System.out.println(top());  // 9
        push(5);
        push(15);
        System.out.println(top());  // 5
        pop();
        System.out.println(top());  // 9
    }

    public static void main(String[] args) {
        test();
    }
}
```

### 최소 힙 구현 정답

```python
heap = [0] * 100005
sz = 0

def push(x):
    global sz
    sz += 1
    heap[sz] = x
    idx = sz
    while idx != 1:
        par = idx // 2
        if heap[par] <= heap[idx]:
            break
        heap[par], heap[idx] = heap[idx], heap[par]
        idx = par

def top():
    return heap[1]

def pop():
    global sz
    heap[1] = heap[sz]
    sz -= 1
    idx = 1
    while idx * 2 <= sz:
        lc = idx * 2
        rc = idx * 2 + 1
        min_child = lc
        if rc <= sz and heap[rc] < heap[lc]:
            min_child = rc
        if heap[idx] <= heap[min_child]:
            break
        heap[idx], heap[min_child] = heap[min_child], heap[idx]
        idx = min_child

def test():
    push(10)
    push(2)
    push(5)
    push(9)
    print(top())  # 2
    pop()
    pop()
    print(top())  # 9
    push(5)
    push(15)
    print(top())  # 5
    pop()
    print(top())  # 9

test()

```

```java
public class MinHeap {
    static int[] heap = new int[100005];
    static int sz = 0;

    static void push(int x) {
        heap[++sz] = x;
        int idx = sz;
        while (idx != 1) {
            int par = idx / 2;
            if (heap[par] <= heap[idx]) break;
            int tmp = heap[par];
            heap[par] = heap[idx];
            heap[idx] = tmp;
            idx = par;
        }
    }

    static int top() {
        return heap[1];
    }

    static void pop() {
        heap[1] = heap[sz--];
        int idx = 1;
        while (idx * 2 <= sz) {
            int lc = idx * 2, rc = idx * 2 + 1;
            int minChild = lc;
            if (rc <= sz && heap[rc] < heap[lc]) minChild = rc;
            if (heap[idx] <= heap[minChild]) break;
            int tmp = heap[idx];
            heap[idx] = heap[minChild];
            heap[minChild] = tmp;
            idx = minChild;
        }
    }

    public static void test() {
        push(10);
        push(2);
        push(5);
        push(9);
        System.out.println(top());  // 2
        pop();
        pop();
        System.out.println(top());  // 9
        push(5);
        push(15);
        System.out.println(top());  // 5
        pop();
        System.out.println(top());  // 9
    }

    public static void main(String[] args) {
        test();
    }
}
```

### BOJ11286: 절댓값 힙

```python
import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
```

```java
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> {
            int absA = Math.abs(a);
            int absB = Math.abs(b);
            if (absA != absB) return absA - absB;
            return a - b; // 음수가 양수보다 먼저 나오도록
        });

        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(br.readLine());
            if (x == 0) {
                if (pq.isEmpty()) System.out.println(0);
                else System.out.println(pq.poll());
            } else {
                pq.add(x);
            }
        }
    }
}
```

### BOJ1715: 카드 정렬하기

```python
import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = [int(input()) for _ in range(n)]
heapq.heapify(heap)
ans = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    cost = a + b
    ans += cost
    heapq.heappush(heap, cost)
print(ans)
```

```java
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < n; i++)
            pq.add(Integer.parseInt(br.readLine()));

        int total = 0;
        while (pq.size() > 1) {
            int a = pq.poll();
            int b = pq.poll();
            int cost = a + b;
            total += cost;
            pq.add(cost);
        }

        System.out.println(total);
    }
}
```