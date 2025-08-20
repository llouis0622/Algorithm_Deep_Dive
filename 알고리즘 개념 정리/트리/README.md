## 1️⃣ 트리

- 무방향이면서 사이클이 없는 연결 그래프
- 연결 그래프이면서 임의의 간선을 제거하면 연결 그래프가 아니게 되는 그래프
- 임의의 두 점을 연결하는 정점이 중복해서 나오지 않는 경로가 유일한 그래프
- V개의 정점을 가지고 V-1개의 간선을 가지는 연결 그래프
- 사이클이 없는 연결 그래프이면서 임의의 간선을 추가하면 사이클이 생기는 그래프
- V개의 정점을 가지고 V-1개의 간선을 가지는 사이클이 없는 그래프

## 2️⃣ 트리 풀이 방법

### **트리 선택 가능성**

- ‘사이클이 없는 연결 그래프’라는 조건이 나올 때
- 부모-자식 관계를 이용할 수 있을 때
- ‘루트 노드에서 시작해서’라는 단서가 있을 때
- 트리 위에서의 경로, 거리, 서브트리 등을 다룰 때

### **트리 문제 판별법**

- N개의 노드, N-1개의 간선 → 무조건 트리
- 루트 노드에서 시작하여 → 트리 기반 탐색
- 각 노드의 부모를 구하라 → DFS/BFS로 부모 저장
- 트리 위에서의 거리, 경로 → DFS, 깊이 배열, LCA
- 자식 노드, 서브트리 → 트리 구조 or DP

### **트리 풀이 기본 흐름**

- 트리 구성하기 – 무방향 그래프처럼 간선을 받아서 트리로 만들기
- 루트 노드 지정 후 DFS or BFS 탐색
- 문제 조건에 맞는 값 저장 – 후위 or 전위 순회 DFS 기반 처리 등

## 3️⃣ 수업 코드

### BFS 예시 코드 1 - 부모 배열 채우기

```python
from collections import deque

adj = [[] for _ in range(10)]
p = [-1] * 10

def bfs(root):
    q = deque()
    q.append(root)
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for nxt in adj[cur]:
            if p[cur] == nxt:
                continue
            q.append(nxt)
            p[nxt] = cur
```

```java
import java.util.*;

public class BFSParent {
    static List<Integer>[] adj = new ArrayList[10];
    static int[] p = new int[10];

    public static void bfs(int root) {
        Queue<Integer> q = new LinkedList<>();
        Arrays.fill(p, -1);  // 초기화
        q.add(root);

        while (!q.isEmpty()) {
            int cur = q.poll();
            System.out.print(cur + " ");
            for (int nxt : adj[cur]) {
                if (p[cur] == nxt) continue;
                q.add(nxt);
                p[nxt] = cur;
            }
        }
    }
}
```

### BFS 예시 코드 2 - 부모와 Depth 배열 채우기

```python
from collections import deque

adj = [[] for _ in range(10)]
p = [-1] * 10
depth = [0] * 10

def bfs(root):
    q = deque()
    q.append(root)
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for nxt in adj[cur]:
            if p[cur] == nxt:
                continue
            q.append(nxt)
            p[nxt] = cur
            depth[nxt] = depth[cur] + 1
```

```java
import java.util.*;

public class BFSDepth {
    static List<Integer>[] adj = new ArrayList[10];
    static int[] p = new int[10];
    static int[] depth = new int[10];

    public static void bfs(int root) {
        Queue<Integer> q = new LinkedList<>();
        Arrays.fill(p, -1);  // 초기화
        q.add(root);

        while (!q.isEmpty()) {
            int cur = q.poll();
            System.out.print(cur + " ");
            for (int nxt : adj[cur]) {
                if (p[cur] == nxt) continue;
                q.add(nxt);
                p[nxt] = cur;
                depth[nxt] = depth[cur] + 1;
            }
        }
    }
}
```

### DFS 예시 코드 1 – 부모와 Depth 배열 채우기, 비재귀

```python
adj = [[] for _ in range(10)]
p = [-1] * 10
depth = [0] * 10

def dfs(root):
    stack = [root]
    while stack:
        cur = stack.pop()
        print(cur, end=' ')
        for nxt in adj[cur]:
            if p[cur] == nxt:
                continue
            stack.append(nxt)
            p[nxt] = cur
            depth[nxt] = depth[cur] + 1
```

```java
import java.util.*;

public class DFSStack {
    static List<Integer>[] adj = new ArrayList[10];
    static int[] p = new int[10];
    static int[] depth = new int[10];

    public static void dfs(int root) {
        Stack<Integer> stack = new Stack<>();
        Arrays.fill(p, -1);
        stack.push(root);

        while (!stack.isEmpty()) {
            int cur = stack.pop();
            System.out.print(cur + " ");
            for (int nxt : adj[cur]) {
                if (p[cur] == nxt) continue;
                stack.push(nxt);
                p[nxt] = cur;
                depth[nxt] = depth[cur] + 1;
            }
        }
    }
}
```

### DFS 예시 코드 2 – 부모와 Depth 배열 채우기, 재귀

```python
adj = [[] for _ in range(10)]
p = [-1] * 10
depth = [0] * 10

def dfs(cur):
    print(cur, end=' ')
    for nxt in adj[cur]:
        if p[cur] == nxt:
            continue
        p[nxt] = cur
        depth[nxt] = depth[cur] + 1
        dfs(nxt)
```

```java
import java.util.*;

public class DFSRecursive {
    static List<Integer>[] adj = new ArrayList[10];
    static int[] p = new int[10];
    static int[] depth = new int[10];

    public static void dfs(int cur) {
        System.out.print(cur + " ");
        for (int nxt : adj[cur]) {
            if (p[cur] == nxt) continue;
            p[nxt] = cur;
            depth[nxt] = depth[cur] + 1;
            dfs(nxt);
        }
    }
}
```

### DFS 예시 코드 3 – 단순 순회, 재귀

```python
adj = [[] for _ in range(10)]

def dfs(cur, par):
    print(cur, end=' ')
    for nxt in adj[cur]:
        if nxt == par:
            continue
        dfs(nxt, cur)
```

```java
import java.util.*;

public class DFSWithParentParam {
    static List<Integer>[] adj = new ArrayList[10];

    public static void dfs(int cur, int par) {
        System.out.print(cur + " ");
        for (int nxt : adj[cur]) {
            if (nxt == par) continue;
            dfs(nxt, cur);
        }
    }
}
```

### 레벨 순회

```python
from collections import deque

lc = [0, 2, 4, 6, 0, 0, 0, 0, 0]
rc = [0, 3, 5, 7, 0, 8, 0, 0, 0]

def bfs():
    q = deque()
    q.append(1)  # root = 1
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        if lc[cur]:
            q.append(lc[cur])
        if rc[cur]:
            q.append(rc[cur])
```

```java
import java.util.*;

public class BinaryTreeBFS {
    static int[] lc = {0, 2, 4, 6, 0, 0, 0, 0, 0};
    static int[] rc = {0, 3, 5, 7, 0, 8, 0, 0, 0};

    public static void bfs() {
        Queue<Integer> q = new LinkedList<>();
        q.add(1); // root = 1
        while (!q.isEmpty()) {
            int cur = q.poll();
            System.out.print(cur + " ");
            if (lc[cur] != 0) q.add(lc[cur]);
            if (rc[cur] != 0) q.add(rc[cur]);
        }
    }

    public static void main(String[] args) {
        bfs();
    }
}
```

### 전위 순회

```python
lc = [0, 2, 4, 6, 0, 0, 0, 0, 0]
rc = [0, 3, 5, 7, 0, 8, 0, 0, 0]

def preorder(cur):
    print(cur, end=' ')
    if lc[cur] != 0:
        preorder(lc[cur])
    if rc[cur] != 0:
        preorder(rc[cur])
```

```java
public class BinaryTreePreorder {
    static int[] lc = {0, 2, 4, 6, 0, 0, 0, 0, 0};
    static int[] rc = {0, 3, 5, 7, 0, 8, 0, 0, 0};

    public static void preorder(int cur) {
        System.out.print(cur + " ");
        if (lc[cur] != 0) preorder(lc[cur]);
        if (rc[cur] != 0) preorder(rc[cur]);
    }

    public static void main(String[] args) {
        preorder(1);
    }
}
```

### 중위 순회

```python
lc = [0, 2, 4, 6, 0, 0, 0, 0, 0]
rc = [0, 3, 5, 7, 0, 8, 0, 0, 0]

def inorder(cur):
    if lc[cur] != 0:
        inorder(lc[cur])
    print(cur, end=' ')
    if rc[cur] != 0:
        inorder(rc[cur])
```

```java
public class BinaryTreeInorder {
    static int[] lc = {0, 2, 4, 6, 0, 0, 0, 0, 0};
    static int[] rc = {0, 3, 5, 7, 0, 8, 0, 0, 0};

    public static void inorder(int cur) {
        if (lc[cur] != 0) inorder(lc[cur]);
        System.out.print(cur + " ");
        if (rc[cur] != 0) inorder(rc[cur]);
    }

    public static void main(String[] args) {
        inorder(1);
    }
}
```

### 후위 순회

```python
lc = [0, 2, 4, 6, 0, 0, 0, 0, 0]
rc = [0, 3, 5, 7, 0, 8, 0, 0, 0]

def postorder(cur):
    if lc[cur] != 0:
        postorder(lc[cur])
    if rc[cur] != 0:
        postorder(rc[cur])
    print(cur, end=' ')
```

```java
public class BinaryTreePostorder {
    static int[] lc = {0, 2, 4, 6, 0, 0, 0, 0, 0};
    static int[] rc = {0, 3, 5, 7, 0, 8, 0, 0, 0};

    public static void postorder(int cur) {
        if (lc[cur] != 0) postorder(lc[cur]);
        if (rc[cur] != 0) postorder(rc[cur]);
        System.out.print(cur + " ");
    }

    public static void main(String[] args) {
        postorder(1);
    }
}
```

### BOJ11725: 트리의 부모 찾기

```python
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
adj = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(root):
    q = deque([root])
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if parent[nxt] == 0:
                parent[nxt] = cur
                q.append(nxt)

bfs(1)
for i in range(2, n + 1):
    print(parent[i])
```

```python
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]
p = [0] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(cur):
    for nxt in adj[cur]:
        if p[cur] == nxt:
            continue
        p[nxt] = cur
        dfs(nxt)

dfs(1)
for i in range(2, n + 1):
    print(p[i])
```

```java
import java.util.*;

public class TreeParent {
    static List<Integer>[] adj;
    static int[] parent;

    public static void bfs(int root) {
        Queue<Integer> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int nxt : adj[cur]) {
                if (parent[nxt] == 0) {
                    parent[nxt] = cur;
                    q.add(nxt);
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        adj = new ArrayList[n + 1];
        parent = new int[n + 1];

        for (int i = 1; i <= n; i++)
            adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v);
            adj[v].add(u);
        }

        bfs(1);

        for (int i = 2; i <= n; i++)
            System.out.println(parent[i]);
    }
}
```

```java
import java.util.*;

public class TreeParentDFS {
    static int n;
    static List<Integer>[] adj;
    static int[] p;

    public static void dfs(int cur) {
        for (int nxt : adj[cur]) {
            if (p[cur] == nxt) continue;
            p[nxt] = cur;
            dfs(nxt);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        adj = new ArrayList[n + 1];
        p = new int[n + 1];

        for (int i = 1; i <= n; i++)
            adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v);
            adj[v].add(u);
        }

        dfs(1);

        for (int i = 2; i <= n; i++)
            System.out.println(p[i]);

        sc.close();
    }
}
```

### BOJ1991: 트리 순회

```python
import sys

input = sys.stdin.readline

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(cur):
    if cur == '.':
        return
    print(cur, end='')
    preorder(tree[cur][0])
    preorder(tree[cur][1])

def inorder(cur):
    if cur == '.':
        return
    inorder(tree[cur][0])
    print(cur, end='')
    inorder(tree[cur][1])

def postorder(cur):
    if cur == '.':
        return
    postorder(tree[cur][0])
    postorder(tree[cur][1])
    print(cur, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
```

```python
import sys

input = sys.stdin.readline

n = int(input())
lc = [0] * 30
rc = [0] * 30
for _ in range(n):
    c, l, r = input().split()
    idx = ord(c) - ord('A') + 1
    if l != '.':
        lc[idx] = ord(l) - ord('A') + 1
    if r != '.':
        rc[idx] = ord(r) - ord('A') + 1

def preorder(cur):
    print(chr(cur + ord('A') - 1), end='')
    if lc[cur]:
        preorder(lc[cur])
    if rc[cur]:
        preorder(rc[cur])

def inorder(cur):
    if lc[cur]:
        inorder(lc[cur])
    print(chr(cur + ord('A') - 1), end='')
    if rc[cur]:
        inorder(rc[cur])

def postorder(cur):
    if lc[cur]:
        postorder(lc[cur])
    if rc[cur]:
        postorder(rc[cur])
    print(chr(cur + ord('A') - 1), end='')

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()
```

```java
import java.util.*;

public class TreeTraversal {
    static Map<Character, char[]> tree = new HashMap<>();

    public static void preorder(char cur) {
        if (cur == '.') return;
        System.out.print(cur);
        preorder(tree.get(cur)[0]);
        preorder(tree.get(cur)[1]);
    }

    public static void inorder(char cur) {
        if (cur == '.') return;
        inorder(tree.get(cur)[0]);
        System.out.print(cur);
        inorder(tree.get(cur)[1]);
    }

    public static void postorder(char cur) {
        if (cur == '.') return;
        postorder(tree.get(cur)[0]);
        postorder(tree.get(cur)[1]);
        System.out.print(cur);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < n; i++) {
            String[] input = sc.nextLine().split(" ");
            char root = input[0].charAt(0);
            char left = input[1].charAt(0);
            char right = input[2].charAt(0);
            tree.put(root, new char[]{left, right});
        }

        preorder('A');
        System.out.println();
        inorder('A');
        System.out.println();
        postorder('A');
    }
}
```

```java
import java.util.*;

public class TreeTraversalArray {
    static int[] lc = new int[30];
    static int[] rc = new int[30];

    public static void preorder(int cur) {
        System.out.print((char) (cur + 'A' - 1));
        if (lc[cur] != 0) preorder(lc[cur]);
        if (rc[cur] != 0) preorder(rc[cur]);
    }

    public static void inorder(int cur) {
        if (lc[cur] != 0) inorder(lc[cur]);
        System.out.print((char) (cur + 'A' - 1));
        if (rc[cur] != 0) inorder(rc[cur]);
    }

    public static void postorder(int cur) {
        if (lc[cur] != 0) postorder(lc[cur]);
        if (rc[cur] != 0) postorder(rc[cur]);
        System.out.print((char) (cur + 'A' - 1));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < n; i++) {
            String[] s = sc.nextLine().split(" ");
            int cur = s[0].charAt(0) - 'A' + 1;
            char l = s[1].charAt(0);
            char r = s[2].charAt(0);
            if (l != '.') lc[cur] = l - 'A' + 1;
            if (r != '.') rc[cur] = r - 'A' + 1;
        }

        preorder(1);
        System.out.println();
        inorder(1);
        System.out.println();
        postorder(1);
        System.out.println();
    }
}
```