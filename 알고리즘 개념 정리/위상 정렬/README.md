## 1️⃣ 위상 정렬

- 방향 그래프에서 간선으로 주어진 정점 간 선후관계를 위배하지 않도록 나열하는 정렬

## 2️⃣ 위상 정렬 풀이 방법

### **위상 정렬 성질**

- 정점과 간선을 실제로 지울 필요 없이 미리 indegree의 값을 저장했다가 매번 뻗어나가는 정점들의 indegree 값만 1 감소시켜도 과정을 수행 가능
- indegree가 0인 정점을 구하기 위해 매번 모든 정점들을 다 확인하는 대신 목록을 따로 저장하고 있다가 직전에 제거한 정점에서 연결된 정점들만 추가

### **위상 정렬 풀이 흐름**

- 맨 처음 모든 간선을 읽으며 indegree 테이블을 채움
- indegree가 0인 정점들을 모두 큐에 넣음
- 큐에서 정점을 꺼내어 위상 정렬 결과에 추가
- 해당 정점으로부터 연결된 모든 정점의 indegree 값을 1 감소시킴. 이때 indegree가 0이 되었다면 그 정점을 큐에 추가
- 큐가 빌 때까지 3, 4번 과정을 반복

## 3️⃣ 수업 코드

### 위상 정렬 구현

- 파이썬
    
    ```python
    import sys
    from collections import deque
    
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        deg[v] += 1
    q = deque(i for i in range(1, n + 1) if deg[i] == 0)
    res = []
    while q:
        cur = q.popleft()
        res.append(cur)
        for nxt in adj[cur]:
            deg[nxt] -= 1
            if deg[nxt] == 0:
                q.append(nxt)
    if len(res) != n:
        print("cycle exists")
    else:
        print(*res)
    ```
    
- 자바
    
    ```java
    import java.io.*;
    import java.util.*;
    
    public class Main {
        public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
    
            List<List<Integer>> adj = new ArrayList<>();
            for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
            int[] deg = new int[n + 1];
    
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                adj.get(u).add(v);
                deg[v]++;
            }
    
            ArrayDeque<Integer> q = new ArrayDeque<>();
            for (int i = 1; i <= n; i++) if (deg[i] == 0) q.add(i);
    
            List<Integer> res = new ArrayList<>();
            while (!q.isEmpty()) {
                int cur = q.poll();
                res.add(cur);
                for (int nxt : adj.get(cur)) {
                    if (--deg[nxt] == 0) q.add(nxt);
                }
            }
    
            if (res.size() != n) System.out.println("cycle exists");
            else {
                StringBuilder sb = new StringBuilder();
                for (int x : res) sb.append(x).append(' ');
                System.out.println(sb.toString().trim());
            }
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
    
        int n, m;
        if (!(cin >> n >> m)) return 0;
        vector<vector<int> > v(n + 1);
        vector<int> deg(n + 1);
    
        for (int i = 0; i < m; i++) {
            int u, w;
            cin >> u >> w;
            v[u].push_back(w);
            deg[w]++;
        }
    
        queue<int> q;
        for (int i = 1; i <= n; i++) if (deg[i] == 0) q.push(i);
    
        vector<int> res;
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            res.push_back(cur);
            for (auto nxt: v[cur]) {
                deg[nxt]--;
                if (deg[nxt] == 0) q.push(nxt);
            }
        }
    
        if ((int) res.size() != n) cout << "cycle exists";
        else {
            for (auto x: res) cout << x << ' ';
        }
    }
    ```
    

### BOJ2252: 줄 세우기

- 파이썬
    
    ```python
    import sys
    from collections import deque
    
    input = sys.stdin.readline
    output = sys.stdout.write
    
    MAX = 32001
    adj = [[] for _ in range(MAX)]
    deg = [0] * MAX
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        deg[b] += 1
    q = deque()
    for i in range(1, n + 1):
        if deg[i] == 0:
            q.append(i)
    while q:
        cur = q.popleft()
        output(f"{cur} ")
        for nxt in adj[cur]:
            deg[nxt] -= 1
            if deg[nxt] == 0:
                q.append(nxt)
    ```
    
- 자바
    
    ```java
    import java.io.*;
    import java.util.*;
    
    public class Main {
        static final int MAX = 32001;
        static ArrayList<Integer>[] adj = new ArrayList[MAX];
        static int[] deg = new int[MAX];
    
        public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
    
            for (int i = 0; i < MAX; i++) adj[i] = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                adj[a].add(b);
                deg[b]++;
            }
    
            ArrayDeque<Integer> q = new ArrayDeque<>();
            for (int i = 1; i <= n; i++) if (deg[i] == 0) q.add(i);
    
            StringBuilder sb = new StringBuilder();
            while (!q.isEmpty()) {
                int cur = q.poll();
                sb.append(cur).append(' ');
                for (int nxt : adj[cur]) {
                    if (--deg[nxt] == 0) q.add(nxt);
                }
            }
            System.out.print(sb.toString());
        }
    }
    ```
    
- C++
    
    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    
    vector<int> adj[32001];
    int deg[32001];
    int n, m;
    
    int main(void) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        cin >> n >> m;
        while (m--) {
            int a, b;
            cin >> a >> b;
            adj[a].push_back(b);
            deg[b]++;
        }
        queue<int> q;
        for (int i = 1; i <= n; i++) {
            if (deg[i] == 0) q.push(i);
        }
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            cout << cur << ' ';
            for (int nxt: adj[cur]) {
                deg[nxt]--;
                if (deg[nxt] == 0) q.push(nxt);
            }
        }
    }
    ```