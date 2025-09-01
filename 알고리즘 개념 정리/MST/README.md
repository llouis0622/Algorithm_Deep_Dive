## 1️⃣ MST

- 신장 트리 중에서 간선의 합이 최소인 트리

## 2️⃣ MST 풀이 방법

### **MST 문제 판별법**

- N개 정점, M개 간선, 모두 연결, 최소 비용
- V-1개 간선으로 연결, 사이클 없이
- 전역적 연결 최소 비용, 최단경로는 한 점에서 다른 점까지
- 가중치가 음수여도 가능
- 간선 가중치가 모두 서로 다르면 MST는 유일

### Kruskal

- 간선을 크기의 오름차순으로 정렬하고 제일 낮은 비용의 간선을 선택
- 현재 선택한 간선이 정점 u, v를 연결하는 간선이라고 할 때 만약 u와 v가 같은 그룹이라면 아무 것도 하지 않고 넘어감, u와 v가 다른 그룹이라면 같은 그룹으로 만들고 현재 선택한 간선을 최소 신장 트리에 추가
- 최소 신장 트리에 V-1개의 간선을 추가시켰다면 과정 종료, 그렇지 않다면 그 다음으로 비용이 작은 간선을 선택한 후 2번 과정 반복

### Prim

- 임의의 정점을 선택해 최소 신장 트리에 추가, 해당 정점과 연결된 모든 간성르 우선순위 큐에 추가
- 우선순위 큐에서 비용이 가장 작은 간선을 선택
- 만약 해당 간선이 최소 신장 트리에 포함된 두 정점을 연결한다면 아무 것도 하지 않고 넘어감, 해당 간선이 최소 신장 트리에 포함된 정점 u와 포함되지 않은 정점 v를 연결한다면 해당 간선과 정점 v를 최소 신장 트리에 추가 후 정점 v와 최소 신장 트리에 포함되지 않는 정점을 연결하는 모든 간선을 우선순위 큐에 추가
- 최소 신장 트리에 V-1개의 간선이 추가될 때까지 2, 3번 과정 반복

## 3️⃣ 수업 코드

### Kruskal

- 파이썬
    
    ```python
    import sys
    
    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def unite(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
        return True
    
    input = sys.stdin.readline
    v, e = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(e)]
    edges.sort()
    parent = list(range(v + 1))
    rank = [0] * (v + 1)
    cnt = 0
    for cost, a, b in edges:
        if not unite(a, b):
            continue
        print(cost, a, b)
        cnt += 1
        if cnt == v - 1:
            break
    ```
    
- 자바
    
    ```java
    import java.io.*;
    import java.util.*;
    
    public class Main {
        static class DSU {
            int[] p, r;
    
            DSU(int n) {
                p = new int[n + 1];
                r = new int[n + 1];
                for (int i = 0; i <= n; i++) p[i] = i;
            }
    
            int find(int x) {
                return p[x] == x ? x : (p[x] = find(p[x]));
            }
    
            boolean isDiffGroup(int a, int b) {
                a = find(a);
                b = find(b);
                if (a == b) return false;
                if (r[a] < r[b]) {
                    int t = a;
                    a = b;
                    b = t;
                }
                p[b] = a;
                if (r[a] == r[b]) r[a]++;
                return true;
            }
        }
    
        public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
    
            List<int[]> edges = new ArrayList<>(e);
            for (int i = 0; i < e; i++) {
                st = new StringTokenizer(br.readLine());
                int cost = Integer.parseInt(st.nextToken());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                edges.add(new int[]{cost, a, b});
            }
            edges.sort(Comparator.comparingInt(x -> x[0]));
    
            DSU dsu = new DSU(v);
            StringBuilder out = new StringBuilder();
            int cnt = 0;
            for (int[] ed : edges) {
                int cost = ed[0], a = ed[1], b = ed[2];
                if (!dsu.isDiffGroup(a, b)) continue;
                out.append(cost).append(' ').append(a).append(' ').append(b).append('\n');
                cnt++;
                if (cnt == v - 1) break;
            }
            System.out.print(out.toString());
        }
    }
    ```
    
- C++
    
    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    
    struct DSU {
        vector<int> p, r;
        DSU(int n): p(n + 1), r(n + 1, 0) { iota(p.begin(), p.end(), 0); }
        int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
    
        bool is_diff_group(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return false;
            if (r[a] < r[b]) swap(a, b);
            p[b] = a;
            if (r[a] == r[b]) r[a]++;
            return true;
        }
    };
    
    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
    
        int v, e;
        if (!(cin >> v >> e)) return 0;
    
        vector<tuple<int, int, int> > edge(e);
        for (int i = 0; i < e; i++) {
            int cost, a, b;
            cin >> cost >> a >> b;
            edge[i] = {cost, a, b};
        }
    
        sort(edge.begin(), edge.end());
        DSU dsu(v);
    
        int cnt = 0;
        for (int i = 0; i < e; i++) {
            int cost, a, b;
            tie(cost, a, b) = edge[i];
            if (!dsu.is_diff_group(a, b)) continue;
            cout << cost << ' ' << a << ' ' << b << '\n';
            cnt++;
            if (cnt == v - 1) break;
        }
    }
    ```
    

### BOJ1197: 최소 스패닝 트리(Kruskal)

- 파이썬
    
    ```python
    import sys
    
    input = sys.stdin.readline
    
    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
        return True
    
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
    edges.sort()
    parent = list(range(V + 1))
    rank = [0] * (V + 1)
    cnt = 0
    ans = 0
    for cost, a, b in edges:
        if union(a, b):
            ans += cost
            cnt += 1
            if cnt == V - 1:
                break
    print(ans)
    ```
    
- 자바
    
    ```java
    import java.io.*;
    import java.util.*;
    
    public class Main {
        static class DSU {
            int[] p, r;
    
            DSU(int n) {
                p = new int[n + 1];
                r = new int[n + 1];
                for (int i = 0; i <= n; i++) p[i] = i;
            }
    
            int find(int x) {
                return p[x] == x ? x : (p[x] = find(p[x]));
            }
    
            boolean unite(int a, int b) {
                a = find(a);
                b = find(b);
                if (a == b) return false;
                if (r[a] < r[b]) {
                    int t = a;
                    a = b;
                    b = t;
                }
                p[b] = a;
                if (r[a] == r[b]) r[a]++;
                return true;
            }
        }
    
        static class Edge {
            int a, b, w;
    
            Edge(int a, int b, int w) {
                this.a = a;
                this.b = b;
                this.w = w;
            }
        }
    
        public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
    
            Edge[] edges = new Edge[E];
            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int w = Integer.parseInt(st.nextToken());
                edges[i] = new Edge(a, b, w);
            }
            Arrays.sort(edges, Comparator.comparingInt(o -> o.w));
    
            DSU dsu = new DSU(V);
            long total = 0;
            int picked = 0;
            for (Edge e1 : edges) {
                if (dsu.unite(e1.a, e1.b)) {
                    total += e1.w;
                    if (++picked == V - 1) break;
                }
            }
            System.out.println(total);
        }
    }
    ```
    
- C++
    
    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    
    struct DSU {
        vector<int> p, r;
        DSU(int n): p(n + 1), r(n + 1, 0) { iota(p.begin(), p.end(), 0); }
        int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
    
        bool unite(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return false;
            if (r[a] < r[b]) swap(a, b);
            p[b] = a;
            if (r[a] == r[b]) r[a]++;
            return true;
        }
    };
    
    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
    
        int V, E;
        if (!(cin >> V >> E)) return 0;
    
        vector<tuple<int, int, int> > edges;
        edges.reserve(E);
        for (int i = 0; i < E; i++) {
            int a, b, w;
            cin >> a >> b >> w;
            edges.emplace_back(w, a, b);
        }
        sort(edges.begin(), edges.end());
    
        DSU dsu(V);
        long long total = 0;
        int picked = 0;
        for (auto &t: edges) {
            int w, a, b;
            tie(w, a, b) = t;
            if (dsu.unite(a, b)) {
                total += w;
                if (++picked == V - 1) break;
            }
        }
        cout << total << '\n';
    }
    ```
    

### Prim

- 파이썬
    
    ```python
    import sys, heapq
    input = sys.stdin.readline
    
    v, e = map(int, input().split())
    adj = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        adj[a].append((c, b))
        adj[b].append((c, a))
    check = [False] * (v + 1)
    pq = []
    check[1] = True
    for cost, nxt in adj[1]:
        heapq.heappush(pq, (cost, 1, nxt))
    cnt = 0
    while cnt < v - 1 and pq:
        cost, a, b = heapq.heappop(pq)
        if check[b]:
            continue
        print(cost, a, b)
        check[b] = True
        cnt += 1
        for c2, nb in adj[b]:
            if not check[nb]:
                heapq.heappush(pq, (c2, b, nb))
    ```
    
- 자바
    
    ```java
    import java.io.*;
    import java.util.*;
    
    public class Main {
        public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
    
            ArrayList<int[]>[] adj = new ArrayList[v + 1];
            for (int i = 0; i <= v; i++) adj[i] = new ArrayList<>();
    
            for (int i = 0; i < e; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                adj[a].add(new int[]{c, b});
                adj[b].add(new int[]{c, a});
            }
    
            boolean[] chk = new boolean[v + 1];
            PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(x -> x[0]));
    
            chk[1] = true;
            for (int[] nx : adj[1]) pq.add(new int[]{nx[0], 1, nx[1]});
    
            StringBuilder out = new StringBuilder();
            int cnt = 0;
            while (cnt < v - 1 && !pq.isEmpty()) {
                int[] t = pq.poll();
                int cost = t[0], a = t[1], b = t[2];
                if (chk[b]) continue;
                out.append(cost).append(' ').append(a).append(' ').append(b).append('\n');
                chk[b] = true;
                cnt++;
                for (int[] nx : adj[b]) if (!chk[nx[1]]) pq.add(new int[]{nx[0], b, nx[1]});
            }
            System.out.print(out.toString());
        }
    }
    ```
    
- C++
    
    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    
    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
    
        int v, e;
        if (!(cin >> v >> e)) return 0;
    
        vector<vector<pair<int, int> > > adj(v + 1);
        for (int i = 0; i < e; i++) {
            int a, b, c;
            cin >> a >> b >> c;
            adj[a].push_back({c, b});
            adj[b].push_back({c, a});
        }
    
        vector<char> chk(v + 1, 0);
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int> >, greater<tuple<int, int, int> > > pq;
    
        chk[1] = 1;
        for (auto &nx: adj[1]) pq.push({nx.first, 1, nx.second});
    
        int cnt = 0;
        while (cnt < v - 1 && !pq.empty()) {
            auto [cost, a, b] = pq.top();
            pq.pop();
            if (chk[b]) continue;
            cout << cost << ' ' << a << ' ' << b << '\n';
            chk[b] = 1;
            cnt++;
            for (auto &nx: adj[b]) if (!chk[nx.second]) pq.push({nx.first, b, nx.second});
        }
    }
    ```
    

### BOJ1197: 최소 스패닝 트리(Prim)

- 파이썬
    
    ```python
    import sys, heapq
    input = sys.stdin.readline
    
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        adj[a].append((c, b))
        adj[b].append((c, a))
    visited = [False] * (V + 1)
    pq = []
    visited[1] = True
    for w, v in adj[1]:
        heapq.heappush(pq, (w, v))
    cnt = 1
    ans = 0
    while cnt < V:
        w, v = heapq.heappop(pq)
        if visited[v]:
            continue
        visited[v] = True
        ans += w
        cnt += 1
        for nw, nv in adj[v]:
            if not visited[nv]:
                heapq.heappush(pq, (nw, nv))
    print(ans)
    ```
    
- 자바
    
    ```java
    import java.io.*;
    import java.util.*;
    
    public class Main {
        public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
    
            ArrayList<int[]>[] adj = new ArrayList[V + 1];
            for (int i = 0; i <= V; i++) adj[i] = new ArrayList<>();
    
            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int w = Integer.parseInt(st.nextToken());
                adj[a].add(new int[]{w, b});
                adj[b].add(new int[]{w, a});
            }
    
            boolean[] vis = new boolean[V + 1];
            PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(x -> x[0]));
    
            vis[1] = true;
            for (int[] e1 : adj[1]) pq.add(new int[]{e1[0], e1[1]});
    
            int picked = 1;
            long total = 0;
            while (picked < V) {
                int[] t = pq.poll();
                int w = t[0], v = t[1];
                if (vis[v]) continue;
                vis[v] = true;
                total += w;
                picked++;
                for (int[] nx : adj[v]) if (!vis[nx[1]]) pq.add(new int[]{nx[0], nx[1]});
            }
            System.out.println(total);
        }
    }
    ```
    
- C++
    
    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    
    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
    
        int V, E;
        if (!(cin >> V >> E)) return 0;
    
        vector<vector<pair<int, int> > > adj(V + 1);
        for (int i = 0; i < E; i++) {
            int a, b, w;
            cin >> a >> b >> w;
            adj[a].push_back({w, b});
            adj[b].push_back({w, a});
        }
    
        vector<char> vis(V + 1, 0);
        priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;
    
        vis[1] = 1;
        for (auto &nx: adj[1]) pq.push({nx.first, nx.second});
    
        int picked = 1;
        long long total = 0;
        while (picked < V) {
            auto [w, v] = pq.top();
            pq.pop();
            if (vis[v]) continue;
            vis[v] = 1;
            total += w;
            picked++;
            for (auto &nx: adj[v]) if (!vis[nx.second]) pq.push({nx.first, nx.second});
        }
    
        cout << total << '\n';
    }
    ```
    

### BOJ1368: 물대기

- 파이썬
    
    ```python
    import sys
    input = sys.stdin.readline
    
    def find(x):
        while x != p[x]:
            p[x] = p[p[x]]
            x = p[x]
        return x
    
    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        if r[a] < r[b]:
            a, b = b, a
        p[b] = a
        if r[a] == r[b]:
            r[a] += 1
        return True
    
    N = int(input().strip())
    W = [0] + [int(input().strip()) for _ in range(N)]
    P = [list(map(int, input().split())) for _ in range(N)]
    edges = []
    for i in range(1, N + 1):
        edges.append((W[i], 0, i))
    for i in range(N):
        for j in range(i + 1, N):
            edges.append((P[i][j], i + 1, j + 1))
    edges.sort()
    p = list(range(N + 1 + 1))
    r = [0] * (N + 1 + 1)
    cnt = 0
    ans = 0
    for w, a, b in edges:
        if union(a, b):
            ans += w
            cnt += 1
            if cnt == N:
                break
    print(ans)
    ```
    
- 자바
    
    ```java
    import java.io.*;
    import java.util.*;
    
    public class Main {
        static class DSU {
            int[] p, r;
    
            DSU(int n) {
                p = new int[n + 1];
                r = new int[n + 1];
                for (int i = 0; i <= n; i++) p[i] = i;
            }
    
            int find(int x) {
                return p[x] == x ? x : (p[x] = find(p[x]));
            }
    
            boolean unite(int a, int b) {
                a = find(a);
                b = find(b);
                if (a == b) return false;
                if (r[a] < r[b]) {
                    int t = a;
                    a = b;
                    b = t;
                }
                p[b] = a;
                if (r[a] == r[b]) r[a]++;
                return true;
            }
        }
    
        static class Edge {
            int w, a, b;
    
            Edge(int w, int a, int b) {
                this.w = w;
                this.a = a;
                this.b = b;
            }
        }
    
        public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int N = Integer.parseInt(br.readLine().trim());
            int[] W = new int[N + 1];
            for (int i = 1; i <= N; i++) W[i] = Integer.parseInt(br.readLine().trim());
            int[][] P = new int[N][N];
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) P[i][j] = Integer.parseInt(st.nextToken());
            }
            ArrayList<Edge> edges = new ArrayList<>();
            for (int i = 1; i <= N; i++) edges.add(new Edge(W[i], 0, i));
            for (int i = 0; i < N; i++) for (int j = i + 1; j < N; j++) edges.add(new Edge(P[i][j], i + 1, j + 1));
            edges.sort(Comparator.comparingInt(o -> o.w));
    
            DSU dsu = new DSU(N + 1);
            long ans = 0;
            int picked = 0;
            for (Edge e : edges) {
                if (dsu.unite(e.a, e.b)) {
                    ans += e.w;
                    if (++picked == N) break;
                }
            }
            System.out.println(ans);
        }
    }
    ```
    
- C++
    
    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    
    struct DSU {
        vector<int> p, r;
        DSU(int n): p(n + 1), r(n + 1, 0) { iota(p.begin(), p.end(), 0); }
        int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
    
        bool unite(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return false;
            if (r[a] < r[b]) swap(a, b);
            p[b] = a;
            if (r[a] == r[b]) r[a]++;
            return true;
        }
    };
    
    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int N;
        if (!(cin >> N)) return 0;
        vector<int> W(N + 1);
        for (int i = 1; i <= N; i++) cin >> W[i];
        vector<vector<int> > P(N, vector<int>(N));
        for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) cin >> P[i][j];
    
        vector<tuple<int, int, int> > edges;
        edges.reserve(N + N * (N - 1) / 2);
        for (int i = 1; i <= N; i++) edges.emplace_back(W[i], 0, i);
        for (int i = 0; i < N; i++) for (int j = i + 1; j < N; j++) edges.emplace_back(P[i][j], i + 1, j + 1);
        sort(edges.begin(), edges.end());
    
        DSU dsu(N + 1);
        long long ans = 0;
        int picked = 0;
        for (auto &t: edges) {
            int w, a, b;
            tie(w, a, b) = t;
            if (dsu.unite(a, b)) {
                ans += w;
                if (++picked == N) break;
            }
        }
        cout << ans << "\n";
    }
    ```