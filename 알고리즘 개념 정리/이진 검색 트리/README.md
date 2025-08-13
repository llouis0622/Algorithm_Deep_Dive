## 1️⃣ 이진 검색 트리

- 왼쪽 서브트리의 모든 값은 부모의 값보다 작고 오른쪽 서브트리의 모든 값은 부모의 값보다 큰 이진 트리

## 2️⃣ 이진 검색 트리 풀이 방법

### **이진 검색 트리 선택 가능성**

- 정렬된 상태로 삽입/삭제/탐색을 빠르게 하고자 함
- 트리 구조 + 정렬된 탐색 + 빠른 연산
- 자료를 정렬된 상태로 유지하면서 동적 연산
- 중위 순회가 정렬된 결과가 됨
- 삽입 순서에 따라 트리 모양이 달라짐

### **이진 검색 트리 문제 판별법**

- 데이터 삽입/삭제 후 정렬 유지 → 트리 기반 정렬 문제
- k번째 원소 찾기 → 순위 트리 응용
- 이분 탐색 응용 → Set/Map 대체
- 최대값, 최소값 빠르게 찾기 → 노드 트래킹

### **이진 검색 트리 풀이 기본 흐름**

- BST 구조 정의 및 삽입 함수
- 탐색 함수 구현 – 원하는 값을 찾을 때까지 트리를 타고 내려감
- 중위 순회 – 정렬된 결과 출력
- 필요 시 삭제 함수 사용

## 3️⃣ 수업 코드

### BOJ7662: 이중 우선순위 큐

```python
import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_q = []
    max_q = []
    visited = [False] * k
    for i in range(k):
        op, num = input().split()
        num = int(num)
        if op == 'I':
            heapq.heappush(min_q, (num, i))
            heapq.heappush(max_q, (-num, i))
            visited[i] = True
        else:
            if num == 1:
                while max_q and not visited[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = False
                    heapq.heappop(max_q)
            else:
                while min_q and not visited[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = False
                    heapq.heappop(min_q)
    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)
    if not min_q or not max_q:
        print("EMPTY")
    else:
        print(-max_q[0][0], min_q[0][0])
```

```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            int k = Integer.parseInt(br.readLine());
            TreeMap<Integer, Integer> map = new TreeMap<>();

            for (int i = 0; i < k; i++) {
                String[] parts = br.readLine().split(" ");
                String op = parts[0];
                int n = Integer.parseInt(parts[1]);

                if (op.equals("I")) {
                    map.put(n, map.getOrDefault(n, 0) + 1);
                } else {
                    if (map.isEmpty()) continue;

                    int key = (n == 1) ? map.lastKey() : map.firstKey();
                    if (map.get(key) == 1) {
                        map.remove(key);
                    } else {
                        map.put(key, map.get(key) - 1);
                    }
                }
            }

            if (map.isEmpty()) {
                System.out.println("EMPTY");
            } else {
                System.out.println(map.lastKey() + " " + map.firstKey());
            }
        }
    }
}
```

### BOJ1202: 보석 도둑

```python
import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewels.sort()
bags.sort()
ans = 0
pq = []
j = 0
for i in bags:
    while j < n and jewels[j][0] <= i:
        heapq.heappush(pq, -jewels[j][1])
        j += 1
    if pq:
        ans += -heapq.heappop(pq)
print(ans)
```

```java
import java.io.*;
import java.util.*;

public class Main {
    static class Jewel implements Comparable<Jewel> {
        int weight, value;

        public Jewel(int weight, int value) {
            this.weight = weight;
            this.value = value;
        }

        public int compareTo(Jewel o) {
            return this.weight - o.weight; // 무게 오름차순
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine()); // 보석 수
        int K = Integer.parseInt(br.readLine()); // 가방 수

        Jewel[] jewels = new Jewel[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            jewels[i] = new Jewel(m, v);
        }

        int[] bags = new int[K];
        for (int i = 0; i < K; i++) {
            bags[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(jewels);         // 무게 순 정렬
        Arrays.sort(bags);           // 가방 무게 정렬

        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder()); // 최대 힙
        long total = 0;
        int j = 0;

        for (int i = 0; i < K; i++) {
            int capacity = bags[i];

            while (j < N && jewels[j].weight <= capacity) {
                pq.offer(jewels[j].value);
                j++;
            }

            if (!pq.isEmpty()) {
                total += pq.poll(); // 가장 비싼 보석
            }
        }

        System.out.println(total);
    }
}
```