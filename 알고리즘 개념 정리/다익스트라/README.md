## 1️⃣ 다익스트라

- 하나의 시작점으로부터 다른 모든 정점까지의 최단 거리를 구하는 알고리즘

### 우선순위 큐를 이용한 다익스트라 알고리즘

- 우선순위 큐에 (0, 시작점)을 추가
- 우선순위 큐에서 거리가 가장 작은 원소를 선택, 해당 거리가 최단 거리 테이블에 있는 값과 다를 경우 3번 과정을 수행하지 않고 넘어감
- 원소가 가리키는 정점을 v라고 할 때, v와 이웃한 정점들에 대해 최단 거리 테이블 값보다 v를 거쳐가는 것이 더 작은 값을 가질 경우 최단 거리 테이블의 값을 갱신하고 우선순위 큐에 (거리, 이웃한 정점의 번호)를 추가
- 우선순위 큐가 빌 때까지 2, 3번 과정을 반복

## 2️⃣ 다익스트라 풀이 방법

### **다익스트라 선택 가능성**

- 가중치 있는 그래프의 최단거리를 물을 때
- 음의 가중치가 없다고 명시된 경우
- 시작 정점이 하나(다중 시작점은 BFS 변형)
- 최단거리와 함께 경로 추적이 필요한 경우

### **다익스트라 문제 판별법**

- 모든 정점으로의 최단 경로 → 다익스트라(단일 시작점)
- 가중치 있음/양의 정수 비용 → 다익스트라 적합
- 최단 거리 + 음수 없음 → 무조건 다익스트라
- 시간, 비용, 거리 최소화 → 최단 거리 문제 가능성 ⬆︎
- 경로를 출력하시오 → 경로 추적 기능 추가
- 정점 수 최대 10만/간선 수 많음 → 우선순위 큐 + 다익스트라

### **다익스트라 풀이 기본 흐름**

- 그래프를 인접 리스트로 저장
- 최단 거리 테이블 초기화
- 우선순위 큐 기반 다익스트라 실행
- 필요 시 경로 추적용 배열 관리

## 3️⃣ 수업 코드

### 다익스트라 개선 전

```python
import sys
import heapq

INF = int(1e9)
V = 10
adj = [[] for _ in range(20005)]
fix = [False] * 20005
d = [INF] * 20005

def dijkstra_naive(st):
    d[st] = 0
    while True:
        idx = -1
        for i in range(1, V + 1):
            if fix[i]:
                continue
            if idx == -1 or d[i] < d[idx]:
                idx = i
        if idx == -1 or d[idx] == INF:
            break
        fix[idx] = True
        for nxt_cost, nxt in adj[idx]:
            d[nxt] = min(d[nxt], d[idx] + nxt_cost)
```

```java
import java.util.*;

public class DijkstraNaive {
    static final int INF = 0x3f3f3f3f;
    static int V = 10;
    static ArrayList<Pair>[] adj = new ArrayList[20005];
    static boolean[] fix = new boolean[20005];
    static int[] d = new int[20005];

    public static void dijkstra_naive(int st) {
        Arrays.fill(d, INF);
        d[st] = 0;

        while (true) {
            int idx = -1;
            for (int i = 1; i <= V; i++) {
                if (fix[i]) continue;
                if (idx == -1 || d[i] < d[idx]) idx = i;
            }

            if (idx == -1 || d[idx] == INF) break;

            fix[idx] = true;
            for (Pair nxt : adj[idx]) {
                d[nxt.v] = Math.min(d[nxt.v], d[idx] + nxt.cost);
            }
        }
    }

    static class Pair {
        int cost, v;

        Pair(int cost, int v) {
            this.cost = cost;
            this.v = v;
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < adj.length; i++) {
            adj[i] = new ArrayList<>();
        }
        
        // 테스트용 그래프 연결 등 추가 가능
    }
}
```

### 다익스트라 우선순위 큐 사용

```python
import heapq

INF = int(1e9)
V = 10
adj = [[] for _ in range(20005)]
d = [INF] * 20005

def dijkstra_heap(st):
    d[st] = 0
    pq = [(0, st)]  # (비용, 정점)
    while pq:
        cost, u = heapq.heappop(pq)
        if d[u] < cost:
            continue
        for nxt_cost, v in adj[u]:
            new_cost = cost + nxt_cost
            if d[v] > new_cost:
                d[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
```

```java
import java.util.*;

public class Dijkstra {
    static final int INF = 0x3f3f3f3f;
    static int V = 10;
    static List<Edge>[] adj = new ArrayList[20005];
    static int[] d = new int[20005];

    static class Edge {
        int v, cost;

        Edge(int v, int cost) {
            this.v = v;
            this.cost = cost;
        }
    }

    static class Node implements Comparable<Node> {
        int v, cost;

        Node(int v, int cost) {
            this.v = v;
            this.cost = cost;
        }

        public int compareTo(Node o) {
            return Integer.compare(this.cost, o.cost);
        }
    }

    public static void dijkstra(int start) {
        Arrays.fill(d, INF);
        d[start] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (d[cur.v] < cur.cost) continue;

            for (Edge edge : adj[cur.v]) {
                int newCost = d[cur.v] + edge.cost;
                if (d[edge.v] > newCost) {
                    d[edge.v] = newCost;
                    pq.offer(new Node(edge.v, newCost));
                }
            }
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < adj.length; i++) {
            adj[i] = new ArrayList<>();
        }
    }
}
```

### BOJ1753: 최단경로

```python
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    distance[start] = 0
    pq = [(0, start)]  # (거리, 정점)
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

dijkstra(K)
for i in range(1, V + 1):
    print("INF" if distance[i] == INF else distance[i])
```

```java
import java.io.*;
import java.util.*;

public class Main {
    static final int INF = 1_000_000_000;
    static int V, E, K;
    static List<Edge>[] adj;
    static int[] dist;

    static class Edge {
        int to, weight;

        Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    static class Node implements Comparable<Node> {
        int v, cost;

        Node(int v, int cost) {
            this.v = v;
            this.cost = cost;
        }

        public int compareTo(Node o) {
            return Integer.compare(this.cost, o.cost);
        }
    }

    static void dijkstra(int start) {
        dist[start] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (dist[cur.v] < cur.cost) continue;

            for (Edge edge : adj[cur.v]) {
                int next = edge.to;
                int cost = cur.cost + edge.weight;

                if (dist[next] > cost) {
                    dist[next] = cost;
                    pq.offer(new Node(next, cost));
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        K = Integer.parseInt(br.readLine());

        adj = new ArrayList[V + 1];
        for (int i = 1; i <= V; i++) adj[i] = new ArrayList<>();

        dist = new int[V + 1];
        Arrays.fill(dist, INF);

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            adj[u].add(new Edge(v, w));
        }

        dijkstra(K);

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= V; i++) {
            sb.append(dist[i] == INF ? "INF" : dist[i]).append('\n');
        }
        System.out.print(sb);
    }
}
```

### 다익스트라 경로 복원

```python
import heapq

INF = int(1e9)

def dijkstra(start, graph, V):
    dist = [INF] * (V + 1)
    prev = [-1] * (V + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cost, u = heapq.heappop(pq)
        if dist[u] < cost:
            continue
        for v, w in graph[u]:
            if dist[v] > cost + w:
                dist[v] = cost + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev

def reconstruct_path(prev, start, end):
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    if path[0] == start:
        return path
    return []
```

```java
import java.util.*;

public class DijkstraPath {
    static final int INF = 1_000_000_000;
    static List<Edge>[] adj;
    static int[] dist, prev;
    static int V;

    static class Edge {
        int to, weight;

        Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    static class Node implements Comparable<Node> {
        int v, cost;

        Node(int v, int cost) {
            this.v = v;
            this.cost = cost;
        }

        public int compareTo(Node o) {
            return Integer.compare(this.cost, o.cost);
        }
    }

    static void dijkstra(int start) {
        dist = new int[V + 1];
        prev = new int[V + 1];
        Arrays.fill(dist, INF);
        Arrays.fill(prev, -1);
        dist[start] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (dist[cur.v] < cur.cost) continue;
            for (Edge e : adj[cur.v]) {
                int cost = dist[cur.v] + e.weight;
                if (dist[e.to] > cost) {
                    dist[e.to] = cost;
                    prev[e.to] = cur.v;
                    pq.offer(new Node(e.to, cost));
                }
            }
        }
    }

    static List<Integer> reconstructPath(int start, int end) {
        List<Integer> path = new ArrayList<>();
        for (int at = end; at != -1; at = prev[at])
            path.add(at);
        Collections.reverse(path);
        if (path.get(0) == start) return path;
        return new ArrayList<>();  // 경로 없음
    }

    public static void main(String[] args) {
        V = 5;
        adj = new ArrayList[V + 1];
        for (int i = 0; i <= V; i++) adj[i] = new ArrayList<>();

        adj[1].add(new Edge(2, 2));
        adj[1].add(new Edge(3, 3));
        adj[2].add(new Edge(3, 4));
        adj[2].add(new Edge(4, 5));
        adj[3].add(new Edge(4, 6));

        dijkstra(1);
        System.out.println(dist[4]);  // 최단 거리: 7
        System.out.println(reconstructPath(1, 4));  // 경로: [1, 2, 4]
    }
}
```

### BOJ11779: 최소비용 구하기 2

```python
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)
prev = [-1] * (n + 1)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
start, end = map(int, input().split())

def dijkstra(start):
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cost, u = heapq.heappop(pq)
        if dist[u] < cost:
            continue
        for v, w in graph[u]:
            new_cost = cost + w
            if dist[v] > new_cost:
                dist[v] = new_cost
                prev[v] = u
                heapq.heappush(pq, (new_cost, v))

def reconstruct_path(start, end):
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path

dijkstra(start)
path = reconstruct_path(start, end)
print(dist[end])
print(len(path))
print(*path)
```

```java
import java.io.*;
import java.util.*;

public class Main {
    static final int INF = 1_000_000_000;
    static int n, m;
    static List<Edge>[] adj;
    static int[] dist, prev;

    static class Edge {
        int to, cost;

        Edge(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
    }

    static class Node implements Comparable<Node> {
        int v, cost;

        Node(int v, int cost) {
            this.v = v;
            this.cost = cost;
        }

        public int compareTo(Node o) {
            return Integer.compare(this.cost, o.cost);
        }
    }

    static void dijkstra(int start) {
        dist[start] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (dist[cur.v] < cur.cost) continue;

            for (Edge e : adj[cur.v]) {
                int next = e.to;
                int newCost = cur.cost + e.cost;
                if (dist[next] > newCost) {
                    dist[next] = newCost;
                    prev[next] = cur.v;
                    pq.offer(new Node(next, newCost));
                }
            }
        }
    }

    static List<Integer> getPath(int start, int end) {
        LinkedList<Integer> path = new LinkedList<>();
        for (int at = end; at != 0; at = prev[at]) {
            path.addFirst(at);
        }
        return path;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new ArrayList<>();

        dist = new int[n + 1];
        prev = new int[n + 1];
        Arrays.fill(dist, INF);

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            adj[u].add(new Edge(v, w));
        }

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        dijkstra(start);
        List<Integer> path = getPath(start, end);

        StringBuilder sb = new StringBuilder();
        sb.append(dist[end]).append("\n");
        sb.append(path.size()).append("\n");
        for (int city : path) sb.append(city).append(" ");
        System.out.println(sb);
    }
}
```