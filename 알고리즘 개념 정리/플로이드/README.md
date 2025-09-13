## 1️⃣ 플로이드

- 모든 정점 쌍 사이의 최단 거리를 구하는 알고리즘

## 2️⃣ 플로이드 풀이 방법

### **플로이드 선택 가능성**

- 그래프의 모든 정점 쌍의 최단 거리를 구해야 할 때
- 음의 간선이 존재할 수 있을 때
- 정점 수가 적은 그래프(N ≤ 500)
- 특정 정점까지의 최단 거리 ×, 모든 정점 쌍이 필요 ◯
- 간선 수가 많아도 가능

### **플로이드 문제 판별법**

- 모든 정점 쌍의 최단 경로 → 플로이드
- 간선에 음수 있음 + 사이클 없음 → 플로이드
- 경로를 지나야 함/중간 정점을 거쳐야 함 → 미리 모든 거리 계산 필요
- 그래프의 거리를 테이블로 출력 → 인접 행렬 기반 플로이드

### **플로이드 풀이 기본 흐름**

- 인접 행렬로 초기화 – dist[i][j] = w(간선 존재 시), dist[i][j] = 0, 나머지는 INF
- 중간 경유지 k를 1부터 N까지 모두 시도
- dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) 수행
- 모든 i, j 쌍에 대해 최단 거리 갱신

## 3️⃣ 수업 코드

### 플로이드 기초 코드

```python
n = int(input())
m = int(input())
INF = int(1e9)
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a - 1][b - 1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
for row in dist:
    print(' '.join(map(lambda x: str(x) if x != INF else 'INF', row)))
```

```java
import java.util.*;

public class FloydWarshall {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();  // 정점 수
        int m = sc.nextInt();  // 간선 수
        int INF = (int) 1e9;

        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++)
            Arrays.fill(dist[i], INF);

        for (int i = 0; i < n; i++)
            dist[i][i] = 0;

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            dist[a - 1][b - 1] = c;  // 1-based 입력을 0-based로 변환
        }

        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][j] == INF) System.out.print("INF ");
                else System.out.print(dist[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```

### BOJ11404: 플로이드

```python
n = int(input())
m = int(input())
INF = int(1e9)
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = min(dist[a][b], c)
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
```

```python
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if dist[a][b] > c:
        dist[a][b] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
```

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int INF = (int) 1e9;

        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++)
            Arrays.fill(dist[i], INF);
        for (int i = 0; i < n; i++)
            dist[i][i] = 0;

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt() - 1;
            int b = sc.nextInt() - 1;
            int c = sc.nextInt();
            dist[a][b] = Math.min(dist[a][b], c);  // 중복 간선 중 최소 비용만 반영
        }

        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][j] == INF) System.out.print("0 ");
                else System.out.print(dist[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```

### 플로이드 경로 복원 코드

```python
n = int(input())
m = int(input())
INF = int(1e9)
dist = [[INF] * n for _ in range(n)]
next_node = [[-1] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if dist[a][b] > c:
        dist[a][b] = c
        next_node[a][b] = b
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                next_node[i][j] = next_node[i][k]

def get_path(u, v):
    if next_node[u][v] == -1:
        return []
    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path

for i in range(n):
    for j in range(n):
        print(0 if dist[i][j] == INF else dist[i][j], end=' ')
    print()
for i in range(n):
    for j in range(n):
        if dist[i][j] == INF or i == j:
            print(0)
        else:
            path = get_path(i, j)
            print(len(path), ' '.join(str(x + 1) for x in path))
```

```java
import java.util.*;

public class Main {
    static final int INF = (int) 1e9;
    static int[][] dist;
    static int[][] next;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        dist = new int[n][n];
        next = new int[n][n];

        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], INF);
            Arrays.fill(next[i], -1);
            dist[i][i] = 0;
        }

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt() - 1;
            int b = sc.nextInt() - 1;
            int c = sc.nextInt();
            if (dist[a][b] > c) {
                dist[a][b] = c;
                next[a][b] = b;
            }
        }

        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                        next[i][j] = next[i][k];
                    }

        // 거리 출력
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][j] == INF) System.out.print("0 ");
                else System.out.print(dist[i][j] + " ");
            }
            System.out.println();
        }

        // 경로 출력
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j || next[i][j] == -1) {
                    System.out.println(0);
                } else {
                    List<Integer> path = getPath(i, j);
                    System.out.print(path.size() + " ");
                    for (int v : path)
                        System.out.print((v + 1) + " ");
                    System.out.println();
                }
            }
        }
    }

    static List<Integer> getPath(int u, int v) {
        List<Integer> path = new ArrayList<>();
        path.add(u);
        while (u != v) {
            u = next[u][v];
            path.add(u);
        }
        return path;
    }
}
```

### BOJ11780: 플로이드 2

```python
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
dist = [[INF] * n for _ in range(n)]
nxt = [[-1] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if dist[a][b] > c:
        dist[a][b] = c
        nxt[a][b] = b
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                nxt[i][j] = nxt[i][k]
for i in range(n):
    for j in range(n):
        print(0 if dist[i][j] == INF else dist[i][j], end=' ')
    print()

def get_path(u, v):
    if nxt[u][v] == -1:
        return []
    path = [u]
    while u != v:
        u = nxt[u][v]
        path.append(u)
    return path

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF or i == j:
            print(0)
        else:
            path = get_path(i, j)
            print(len(path), ' '.join(str(x + 1) for x in path))
```

```java
import java.util.*;

public class Main {
    static final int INF = (int) 1e9;
    static int[][] dist;
    static int[][] next;
    static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int m = sc.nextInt();

        dist = new int[n][n];
        next = new int[n][n];

        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], INF);
            Arrays.fill(next[i], -1);
            dist[i][i] = 0;
        }

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt() - 1;
            int b = sc.nextInt() - 1;
            int c = sc.nextInt();
            if (dist[a][b] > c) {
                dist[a][b] = c;
                next[a][b] = b;
            }
        }

        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                        next[i][j] = next[i][k];
                    }

        // 거리 출력
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][j] == INF) System.out.print("0 ");
                else System.out.print(dist[i][j] + " ");
            }
            System.out.println();
        }

        // 경로 출력
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][j] == INF || i == j) {
                    System.out.println(0);
                } else {
                    List<Integer> path = getPath(i, j);
                    System.out.print(path.size() + " ");
                    for (int v : path)
                        System.out.print((v + 1) + " ");
                    System.out.println();
                }
            }
        }
    }

    static List<Integer> getPath(int u, int v) {
        List<Integer> path = new ArrayList<>();
        path.add(u);
        while (u != v) {
            u = next[u][v];
            path.add(u);
        }
        return path;
    }
}
```