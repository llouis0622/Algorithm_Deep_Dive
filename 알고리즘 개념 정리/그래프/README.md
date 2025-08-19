## 1️⃣ 그래프

- 정점과 간선으로 이루어진 자료구조
- 무방향 그래프 : 방향성이 없는 그래프
- 방향 그래프 : 방향성이 있는 그래프
- 순환 그래프 : 순환 구조가 있는 그래프
- 비순환 그래프 : 순환 구조가 없는 그래프
- 완전 그래프 : 모든 서로 다른 두 정점 쌍이 간선으로 연결된 그래프
- 연결 그래프 : 임의의 두 정점 사이에 경로가 항상 존재하는 그래프
- 단순 그래프 : 두 정점 사이의 간선이 1개 이하이고 루프가 존재하지 않는 그래프

## 2️⃣ 그래프 풀이 방법

### **그래프 선택 가능성**

- 노드와 연결 관계가 명확할 때
- 방향, 연결, 순서, 경로, 거리 등이 문제에서 언급될 때
- 그래프 자료구조를 주는 경우

### **그래프 문제 판별법**

- 정점, 간선, 노드, 연결 → 그래프 구조 제시
- 이동, 길, 경로, 거리 → 경로 탐색 문제
- 연결되어 있는가, 도달 가능한가 → DFS/BFS 탐색
- 사이클, 순환 여부, 트리 → DFS, 유니온 파인드
- 순서, 선행 조건, 일정표 → 위상 정렬

### **그래프 풀이 기본 흐름**

- 입력 파싱 – 인접 리스트 or 행렬로 그래프 구성
- DFS or BFS 등으로 탐색 구조 선택
- 방문 체크, 결과 저장, 종료 조건 처리

## 3️⃣ 수업 코드

### 방향 그래프 - 인접 행렬

```python
v, e = map(int, input().split())
adj_matrix = [[0] * 10 for _ in range(10)]
for _ in range(e):
    u, v = map(int, input().split())
    adj_matrix[u][v] = 1
```

```java
import java.util.Scanner;

public class DirectedGraphMatrix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int v = sc.nextInt();
        int e = sc.nextInt();

        int[][] adjMatrix = new int[10][10];
        for (int i = 0; i < e; i++) {
            int u = sc.nextInt();
            int w = sc.nextInt();
            adjMatrix[u][w] = 1;
        }

        sc.close();
    }
}
```

### 무방향 그래프 - 인접 행렬

```python
v, e = map(int, input().split())
adj_matrix = [[0] * 10 for _ in range(10)]
for _ in range(e):
    u, v = map(int, input().split())
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1
```

```java
import java.util.Scanner;

public class UndirectedGraphMatrix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int v = sc.nextInt();
        int e = sc.nextInt();

        int[][] adjMatrix = new int[10][10];
        for (int i = 0; i < e; i++) {
            int u = sc.nextInt();
            int w = sc.nextInt();
            adjMatrix[u][w] = 1;
            adjMatrix[w][u] = 1;
        }

        sc.close();
    }
}
```

### 방향 그래프 - 인접 리스트

```python
v, e = map(int, input().split())
adj = [[] for _ in range(10)]
for _ in range(e):
    u, v = map(int, input().split())
    adj[u].append(v)
```

```java
import java.util.*;

public class DirectedGraphList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int v = sc.nextInt();
        int e = sc.nextInt();

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < 10; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < e; i++) {
            int u = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(w);
        }

        sc.close();
    }
}
```

### 무방향 그래프 - 인접 리스트

```python
v, e = map(int, input().split())
adj = [[] for _ in range(10)]
for _ in range(e):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
```

```java
import java.util.*;

public class UndirectedGraphList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int v = sc.nextInt();
        int e = sc.nextInt();

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < 10; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < e; i++) {
            int u = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(w);
            adj.get(w).add(u);
        }

        sc.close();
    }
}
```

### 방향 그래프 - 인접 리스트 & 라이브러리 없이

```python
v = int(input())
e = int(input())
edge = [list(map(int, input().split())) for _ in range(e)]
deg = [0] * 10
for u, v_ in edge:
    deg[u] += 1
adj = [[] for _ in range(10)]
idx = [0] * 10
for _ in range(10):
    adj[_] = [0] * deg[_]
for u, v_ in edge:
    adj[u][idx[u]] = v_
    idx[u] += 1
```

```java
import java.util.Scanner;

public class DirectedGraphArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] edge = new int[10][2];
        int[] deg = new int[10];
        int[][] adj = new int[10][];
        int[] idx = new int[10];

        int v = sc.nextInt();
        int e = sc.nextInt();

        for (int i = 0; i < e; i++) {
            edge[i][0] = sc.nextInt();
            edge[i][1] = sc.nextInt();
            deg[edge[i][0]]++;
        }

        for (int i = 1; i <= v; i++)
            adj[i] = new int[deg[i]];

        for (int i = 0; i < e; i++) {
            int u = edge[i][0], w = edge[i][1];
            adj[u][idx[u]++] = w;
        }

        sc.close();
    }
}
```

### 무방향 그래프 - 인접 리스트 & 라이브러리 없이

```python
v = int(input())
e = int(input())
edge = [list(map(int, input().split())) for _ in range(e)]
deg = [0] * 10
for u, v_ in edge:
    deg[u] += 1
    deg[v_] += 1
adj = [[] for _ in range(10)]
idx = [0] * 10
for _ in range(10):
    adj[_] = [0] * deg[_]
for u, v_ in edge:
    adj[u][idx[u]] = v_
    idx[u] += 1
    adj[v_][idx[v_]] = u
    idx[v_] += 1
```

```java
import java.util.Scanner;

public class UndirectedGraphArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] edge = new int[10][2];
        int[] deg = new int[10];
        int[][] adj = new int[10][];
        int[] idx = new int[10];

        int v = sc.nextInt();
        int e = sc.nextInt();

        for (int i = 0; i < e; i++) {
            edge[i][0] = sc.nextInt();
            edge[i][1] = sc.nextInt();
            deg[edge[i][0]]++;
            deg[edge[i][1]]++;
        }

        for (int i = 1; i <= v; i++)
            adj[i] = new int[deg[i]];

        for (int i = 0; i < e; i++) {
            int u = edge[i][0], w = edge[i][1];
            adj[u][idx[u]++] = w;
            adj[w][idx[w]++] = u;
        }

        sc.close();
    }
}
```

### **BFS 예시 코드 1 – 연결 그래프에서의 순회**

```python
from collections import deque

adj = [[] for _ in range(10)]
vis = [False] * 10

def bfs():
    q = deque()
    q.append(1)
    vis[1] = True
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for nxt in adj[cur]:
            if vis[nxt]:
                continue
            q.append(nxt)
            vis[nxt] = True
```

```java
import java.util.*;

public class BFSExample {
    static List<Integer>[] adj = new ArrayList[10];
    static boolean[] vis = new boolean[10];

    public static void bfs() {
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        vis[1] = true;
        while (!q.isEmpty()) {
            int cur = q.peek();
            q.poll();
            System.out.print(cur + " ");
            for (int nxt : adj[cur]) {
                if (vis[nxt]) continue;
                q.add(nxt);
                vis[nxt] = true;
            }
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < 10; i++)
            adj[i] = new ArrayList<>();

        // 예시용 간선 추가
        // adj[1].add(2); ...

        bfs();
    }
}
```

### **BFS 예시 코드 2 – 연결 그래프에서 1번 정점과의 거리**

```python
from collections import deque

adj = [[] for _ in range(10)]
dist = [-1] * 10

def bfs():
    q = deque()
    q.append(1)
    dist[1] = 0
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if dist[nxt] != -1:
                continue
            q.append(nxt)
            dist[nxt] = dist[cur] + 1
```

```java
import java.util.*;

public class BFSShortestDistance {
    static List<Integer>[] adj = new ArrayList[10];
    static int[] dist = new int[10];

    public static void bfs() {
        Arrays.fill(dist, -1);
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        dist[1] = 0;

        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int nxt : adj[cur]) {
                if (dist[nxt] != -1) continue;
                q.add(nxt);
                dist[nxt] = dist[cur] + 1;
            }
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) adj[i] = new ArrayList<>();

        // 간선 예시 (연결 그래프)

        bfs();
    }
}
```

### **BFS 예시 코드 3 – 연결 그래프가 아닐 때 순회**

```python
from collections import deque

adj = [[] for _ in range(10)]
vis = [False] * 10
v = 9

def bfs():
    for i in range(1, v + 1):
        if vis[i]:
            continue
        q = deque()
        q.append(i)
        vis[i] = True
        while q:
            cur = q.popleft()
            print(cur, end=' ')
            for nxt in adj[cur]:
                if vis[nxt]:
                    continue
                q.append(nxt)
                vis[nxt] = True
```

```java
import java.util.*;

public class MultiComponentBFS {
    static List<Integer>[] adj = new ArrayList[10];
    static boolean[] vis = new boolean[10];
    static int v = 9;

    public static void bfs() {
        for (int i = 1; i <= v; i++) {
            if (vis[i]) continue;
            Queue<Integer> q = new LinkedList<>();
            q.add(i);
            vis[i] = true;

            while (!q.isEmpty()) {
                int cur = q.poll();
                System.out.print(cur + " ");
                for (int nxt : adj[cur]) {
                    if (vis[nxt]) continue;
                    q.add(nxt);
                    vis[nxt] = true;
                }
            }
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < 10; i++)
            adj[i] = new ArrayList<>();

        // 예시 연결 (예: 여러 연결 요소)

        bfs();
    }
}
```

### **DFS 예시 코드 1 – 연결 그래프에서의 순회, 비재귀**

```python
adj = [[] for _ in range(10)]
vis = [False] * 10

def dfs():
    stack = []
    stack.append(1)
    vis[1] = True
    while stack:
        cur = stack.pop()
        print(cur, end=' ')
        for nxt in adj[cur]:
            if vis[nxt]:
                continue
            stack.append(nxt)
            vis[nxt] = True
```

```java
import java.util.*;

public class DFSIterative {
    static List<Integer>[] adj = new ArrayList[10];
    static boolean[] vis = new boolean[10];

    public static void dfs() {
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        vis[1] = true;

        while (!stack.isEmpty()) {
            int cur = stack.pop();
            System.out.print(cur + " ");
            for (int nxt : adj[cur]) {
                if (vis[nxt]) continue;
                stack.push(nxt);
                vis[nxt] = true;
            }
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < 10; i++)
            adj[i] = new ArrayList<>();

        // 예시 간선 추가

        dfs();
    }
}
```

### **DFS 예시 코드 2 – 연결 그래프에서의 순회, 재귀**

```python
adj = [[] for _ in range(10)]
vis = [False] * 10

def dfs(cur):
    vis[cur] = True
    print(cur, end=' ')
    for nxt in adj[cur]:
        if vis[nxt]:
            continue
        dfs(nxt)
```

```java
import java.util.*;

public class DFSRecursive {
    static List<Integer>[] adj = new ArrayList[10];
    static boolean[] vis = new boolean[10];

    public static void dfs(int cur) {
        vis[cur] = true;
        System.out.print(cur + " ");
        for (int nxt : adj[cur]) {
            if (vis[nxt]) continue;
            dfs(nxt);
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < 10; i++)
            adj[i] = new ArrayList<>();

        // 예시 간선 추가
        
        dfs(1);
    }
}
```

### **DFS 예시 코드 3 – 연결 그래프에서의 순회, 비재귀 2**

```python
adj = [[] for _ in range(10)]
vis = [False] * 10

def dfs():
    stack = []
    stack.append(1)
    while stack:
        cur = stack.pop()
        if vis[cur]:
            continue
        vis[cur] = True
        print(cur, end=' ')
        for nxt in adj[cur]:
            if not vis[nxt]:
                stack.append(nxt)
```

```java
import java.util.*;

public class DFSIterativeAlt {
    static List<Integer>[] adj = new ArrayList[10];
    static boolean[] vis = new boolean[10];

    public static void dfs() {
        Stack<Integer> stack = new Stack<>();
        stack.push(1);

        while (!stack.isEmpty()) {
            int cur = stack.pop();
            if (vis[cur]) continue;
            vis[cur] = true;
            System.out.print(cur + " ");
            for (int nxt : adj[cur]) {
                if (!vis[nxt]) stack.push(nxt);
            }
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < 10; i++)
            adj[i] = new ArrayList<>();

        // 예시 간선 추가

        dfs();
    }
}
```

### BOJ11724: 연결 요소의 개수

```python
from collections import deque
import sys

input = sys.stdin.readline

adj = [[] for _ in range(1005)]
vis = [False] * 1005
n, m = map(int, input().split())
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
num = 0
for i in range(1, n + 1):
    if vis[i]:
        continue
    num += 1
    q = deque()
    q.append(i)
    vis[i] = True
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if vis[nxt]:
                continue
            q.append(nxt)
            vis[nxt] = True
print(num)
```

```java
import java.util.*;

public class Main {
    static List<Integer>[] adj = new ArrayList[1005];
    static boolean[] vis = new boolean[1005];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        for (int i = 0; i <= 1000; i++)
            adj[i] = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj[u].add(v);
            adj[v].add(u);
        }

        int num = 0;
        for (int i = 1; i <= n; i++) {
            if (vis[i]) continue;
            num++;
            Queue<Integer> q = new LinkedList<>();
            q.add(i);
            vis[i] = true;

            while (!q.isEmpty()) {
                int cur = q.poll();
                for (int nxt : adj[cur]) {
                    if (vis[nxt]) continue;
                    q.add(nxt);
                    vis[nxt] = true;
                }
            }
        }

        System.out.println(num);
        sc.close();
    }
}
```

### BOJ1260: DFS와 BFS

```python
from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, w = map(int, input().split())
    adj[u].append(w)
    adj[w].append(u)
for i in range(1, n + 1):
    adj[i].sort()

def bfs(start):
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for nxt in adj[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

def dfs(cur, visited):
    visited[cur] = True
    print(cur, end=' ')
    for nxt in adj[cur]:
        if not visited[nxt]:
            dfs(nxt, visited)

dfs_visited = [False] * (n + 1)
dfs(v, dfs_visited)
print()
bfs(v)
```

```java
import java.util.*;

public class Main {
    static List<Integer>[] adj;
    static boolean[] visited;
    static int n;

    public static void dfs(int cur) {
        visited[cur] = true;
        System.out.print(cur + " ");
        for (int nxt : adj[cur]) {
            if (!visited[nxt]) dfs(nxt);
        }
    }

    public static void bfs(int start) {
        boolean[] vis = new boolean[n + 1];
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        vis[start] = true;

        while (!q.isEmpty()) {
            int cur = q.poll();
            System.out.print(cur + " ");
            for (int nxt : adj[cur]) {
                if (!vis[nxt]) {
                    vis[nxt] = true;
                    q.add(nxt);
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int m = sc.nextInt();
        int v = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++)
            adj[i] = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int w = sc.nextInt();
            adj[u].add(w);
            adj[w].add(u);
        }

        for (int i = 1; i <= n; i++)
            Collections.sort(adj[i]);

        visited = new boolean[n + 1];
        dfs(v);
        System.out.println();
        bfs(v);
        sc.close();
    }
}
```