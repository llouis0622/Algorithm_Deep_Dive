## 1️⃣ Union-Find

- Union : 두 그룹을 합치는 연산
- Find : 원소가 속해 있는 그룹을 알아내는 연산

## 2️⃣ Union-Find 최적화

- Union by rank : 두 집합을 합칠 때 작은 트리를 큰 트리에 달기 → 트리 높이가 커지는 것 방지
- 경로 압축 : 루트를 찾은 뒤 거쳐간 모든 노드의 부모를 루트로 바꿈 → 다음 find가 빨라짐

## 3️⃣ 수업 코드

### Find 연산

- 파이썬
    
    ```python
    p = [-1] * 11
    
    def find(x):
        if p[x] < 0:
            return x
        p[x] = find(p[x])
        return p[x]
    ```
    
- 자바
    
    ```java
    import java.util.*;
    
    public class Main {
        static int[] p = new int[11];
    
        static int find(int x) {
            if (p[x] < 0) return x;
            return p[x] = find(p[x]);
        }
    
        public static void main(String[] args) {
            Arrays.fill(p, -1);
        }
    }
    ```
    
- C++
    
    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    
    vector<int> p(11, -1);
    
    int find(int x) {
        if (p[x] < 0) return x;
        return p[x] = find(p[x]);
    }
    ```
    

### Union 연산

- 파이썬
    
    ```python
    def union(u, v):
        u = find(u)
        v = find(v)
        if u == v:
            return False
        p[v] = u
        return True
    ```
    
- 자바
    
    ```java
    import java.util.*;
    
    public class Main {
        static int[] p = new int[11];
    
        static int find(int x) {
            while (p[x] > 0) x = p[x];
            return x;
        }
    
        static boolean uni(int u, int v) {
            u = find(u);
            v = find(v);
            if (u == v) return false;
            p[v] = u;
            return true;
        }
    
        public static void main(String[] args) {
            Arrays.fill(p, -1);
        }
    }
    ```
    
- C++
    
    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    
    vector<int> p(11, -1);
    
    int find(int x) {
        while (p[x] > 0) x = p[x];
        return x;
    }
    
    bool uni(int u, int v) {
        u = find(u);
        v = find(v);
        if (u == v) return false;
        p[v] = u;
        return true;
    }
    
    int main() {
    }
    ```
    

### Union by rank

- 파이썬
    
    ```python
    def union(u, v):
        u = find(u)
        v = find(v)
        if u == v:
            return False
        if p[v] < p[u]:
            u, v = v, u
        if p[u] == p[v]:
            p[u] -= 1
        p[v] = u
        return True
    ```
    
- 자바
    
    ```java
    import java.util.*;
    
    public class Main {
        static int[] p = new int[11];
    
        static int find(int x) {
            if (p[x] < 0) return x;
            return p[x] = find(p[x]);
        }
    
        static boolean uni(int u, int v) {
            u = find(u);
            v = find(v);
            if (u == v) return false;
            if (p[v] < p[u]) {
                int tmp = u;
                u = v;
                v = tmp;
            }
            if (p[u] == p[v]) p[u]--;
            p[v] = u;
            return true;
        }
    
        public static void main(String[] args) {
            Arrays.fill(p, -1);
        }
    }
    ```
    
- C++
    
    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    
    vector<int> p(11, -1);
    
    int find(int x) {
        if (p[x] < 0) return x;
        return p[x] = find(p[x]);
    }
    
    bool uni(int u, int v) {
        u = find(u);
        v = find(v);
        if (u == v) return false;
        if (p[v] < p[u]) swap(u, v);
        if (p[u] == p[v]) p[u]--;
        p[v] = u;
        return true;
    }
    
    int main() {
    }
    ```
    

### 경로 압축

- 파이썬
    
    ```python
    def union(u, v):
        u = find(u)
        v = find(v)
        if u == v:
            return False
        if p[v] < p[u]:
            u, v = v, u
        if p[u] == p[v]:
            p[u] -= 1
        p[v] = u
        return True
    ```
    
- 자바
    
    ```java
    import java.util.*;
    
    public class Main {
        static int[] p = new int[11];
    
        static int find(int x) {
            if (p[x] < 0) return x;
            return p[x] = find(p[x]); // 경로 압축
        }
    
        static boolean uni(int u, int v) {
            u = find(u);
            v = find(v);
            if (u == v) return false;
            if (p[v] < p[u]) {
                int tmp = u;
                u = v;
                v = tmp;
            }
            if (p[u] == p[v]) p[u]--;
            p[v] = u;
            return true;
        }
    
        public static void main(String[] args) {
            Arrays.fill(p, -1);
        }
    }
    ```
    
- C++
    
    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    
    vector<int> p(11, -1);
    
    int find(int x) {
        if (p[x] < 0) return x;
        return p[x] = find(p[x]);
    }
    
    bool uni(int u, int v) {
        u = find(u);
        v = find(v);
        if (u == v) return false;
        if (p[v] < p[u]) swap(u, v);
        if (p[u] == p[v]) p[u]--;
        p[v] = u;
        return true;
    }
    
    int main() {
    }
    ```
    

### BOJ1717: 집합의 표현

- 파이썬
    
    ```python
    import sys
    
    input = sys.stdin.readline
    ansput = sys.stdans.write
    
    n, m = map(int, input().split())
    p = [-1] * (n + 1)
    
    def find(x):
        r = x
        while p[r] >= 0:
            r = p[r]
        while x != r:
            px = p[x]
            p[x] = r
            x = px
        return r
    
    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        if p[a] > p[b]:
            a, b = b, a
        p[a] += p[b]
        p[b] = a
        return True
    
    ans = []
    for _ in range(m):
        t, a, b = map(int, input().split())
        if t == 0:
            union(a, b)
        else:
            ans.append("YES\n" if find(a) == find(b) else "NO\n")
    ansput(''.join(ans))
    ```
    
- 자바
    
    ```java
    import java.io.*;
    import java.util.*;
    
    public class Main {
        static int[] p;
    
        static int find(int x) {
            int r = x;
            while (p[r] >= 0) r = p[r];
            while (x != r) {
                int px = p[x];
                p[x] = r;
                x = px;
            }
            return r;
        }
    
        static void unite(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return;
            if (p[a] > p[b]) {
                int t = a;
                a = b;
                b = t;
            }
            p[a] += p[b];
            p[b] = a;
        }
    
        public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringBuilder sb = new StringBuilder();
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            p = new int[n + 1];
            Arrays.fill(p, -1);
    
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int t = Integer.parseInt(st.nextToken());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                if (t == 0) {
                    unite(a, b);
                } else {
                    sb.append(find(a) == find(b) ? "YES\n" : "NO\n");
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
    
    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
    
        int n, m;
        if (!(cin >> n >> m)) return 0;
        vector<int> p(n + 1, -1);
    
        auto find = [&](int x) {
            int r = x;
            while (p[r] >= 0) r = p[r];
            while (x != r) {
                int px = p[x];
                p[x] = r;
                x = px;
            }
            return r;
        };
    
        auto unite = [&](int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return;
            if (p[a] > p[b]) swap(a, b);
            p[a] += p[b];
            p[b] = a;
        };
    
        string out;
        out.reserve(m * 4);
        for (int i = 0; i < m; i++) {
            int t, a, b;
            cin >> t >> a >> b;
            if (t == 0) unite(a, b);
            else out += (find(a) == find(b) ? "YES\n" : "NO\n");
        }
        cout << out;
    }
    ```
    

### BOJ7511: 소셜 네트워킹 어플리케이션

- 파이썬
    
    ```python
    import sys
    input = sys.stdin.readline
    
    def find(x):
        while p[x] >= 0:
            if p[p[x]] >= 0:
                p[x] = p[p[x]]
            x = p[x]
        return x
    
    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return
        if p[a] > p[b]:
            a, b = b, a
        p[a] += p[b]
        p[b] = a
    
    T = int(input())
    ans = []
    for i in range(1, T + 1):
        n = int(input())
        k = int(input())
        p = [-1] * n
        for _ in range(k):
            a, b = map(int, input().split())
            union(a, b)
        m = int(input())
        ans.append(f"Scenario {i}:")
        for _ in range(m):
            u, v = map(int, input().split())
            ans.append("1" if find(u) == find(v) else "0")
        if i != T:
            ans.append("")
    print("\n".join(ans))
    ```
    
- 자바
    
    ```java
    import java.io.*;
    import java.util.*;
    
    public class Main {
        static int[] p;
    
        static int find(int x) {
            int r = x;
            while (p[r] >= 0) r = p[r];
            while (x != r) {
                int px = p[x];
                p[x] = r;
                x = px;
            }
            return r;
        }
    
        static void unite(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return;
            if (p[a] > p[b]) {
                int t = a;
                a = b;
                b = t;
            }
            p[a] += p[b];
            p[b] = a;
        }
    
        public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringBuilder sb = new StringBuilder();
            int T = Integer.parseInt(br.readLine());
            for (int tc = 1; tc <= T; tc++) {
                int n = Integer.parseInt(br.readLine());
                int k = Integer.parseInt(br.readLine());
                p = new int[n];
                Arrays.fill(p, -1);
                for (int i = 0; i < k; i++) {
                    StringTokenizer st = new StringTokenizer(br.readLine());
                    int a = Integer.parseInt(st.nextToken());
                    int b = Integer.parseInt(st.nextToken());
                    unite(a, b);
                }
                int m = Integer.parseInt(br.readLine());
                sb.append("Scenario ").append(tc).append(":\n");
                for (int i = 0; i < m; i++) {
                    StringTokenizer st = new StringTokenizer(br.readLine());
                    int u = Integer.parseInt(st.nextToken());
                    int v = Integer.parseInt(st.nextToken());
                    sb.append(find(u) == find(v) ? '1' : '0').append('\n');
                }
                if (tc != T) sb.append('\n');
            }
            System.out.print(sb.toString());
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
    
        int T;
        cin >> T;
        for (int tc = 1; tc <= T; tc++) {
            int n, k;
            cin >> n >> k;
            vector<int> p(n, -1);
    
            function<int(int)> find = [&](int x) {
                int r = x;
                while (p[r] >= 0) r = p[r];
                while (x != r) {
                    int px = p[x];
                    p[x] = r;
                    x = px;
                }
                return r;
            };
            auto unite = [&](int a, int b) {
                a = find(a);
                b = find(b);
                if (a == b) return;
                if (p[a] > p[b]) swap(a, b);
                p[a] += p[b];
                p[b] = a;
            };
    
            for (int i = 0; i < k; i++) {
                int a, b;
                cin >> a >> b;
                unite(a, b);
            }
            int m;
            cin >> m;
            cout << "Scenario " << tc << ":\n";
            for (int i = 0; i < m; i++) {
                int u, v;
                cin >> u >> v;
                cout << (find(u) == find(v) ? 1 : 0) << '\n';
            }
            if (tc != T) cout << '\n';
        }
    }
    ```