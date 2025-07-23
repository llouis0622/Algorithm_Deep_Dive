## 1️⃣ DP

- 여러 개의 하위 문제를 먼저 푼 후 그 결과를 쌓아 올려 주어진 문제를 해결하는 알고리즘

## 2️⃣ DP 풀이 방법

### **DP 선택 가능성**

- 작은 문제로 쪼갤 수 있는가
- 같은 부분 문제를 계속 계산하는가
- 이전에 계산한 결과로 다음 계산이 가능한가
- 중복 호출이 많은가

### **DP 문제 판별법**

- 동일한 하위 문제를 여러 번 계산 → DP 필수
- 작은 문제의 최적해로 큰 문제 풀 수 있음 → DP
- 조건이 최대, 최소, 경우의 수 → DP 가능성 높음
- 단순한 그리디/완전탐색으로는 시간초과 → DP로 최적화

### **DP 풀이 기본 흐름**

- 상태 정의 - dp[i]가 무슨 의미인지 명확히 파악
- 점화식 세우기 - dp[i]가 이전 상태와 어떤 관계인지 파악
- 초기값 세팅 - Base Case가 DP의 시작점
- Bottom-up or Top-down 선택 - 반복문 or 재귀 + 메모이제이션
- 배열/메모 테이블 채우기 - 테이블에 중간 결과 저장

## 3️⃣ 수업 코드

### BOJ1463: 1로 만들기

```python
n = int(input())
dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
print(dp[n])
```

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[n + 1];
        dp[1] = 0;

        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + 1;

            if (i % 2 == 0) {
                dp[i] = Math.min(dp[i], dp[i / 2] + 1);
            }

            if (i % 3 == 0) {
                dp[i] = Math.min(dp[i], dp[i / 3] + 1);
            }
        }

        System.out.println(dp[n]);
    }
}
```

### BOJ9095: 1, 2, 3 더하기

```python
t = int(input())
dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for _ in range(t):
    n = int(input())
    print(dp[n])
```

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        int[] dp = new int[12];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        for (int i = 4; i <= 11; i++) {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
        }

        for (int t = 0; t < T; t++) {
            int n = Integer.parseInt(br.readLine());
            System.out.println(dp[n]);
        }
    }
}
```

### BOJ2579: 계단 오르기

```python
n = int(input())
s = [0] + [int(input()) for _ in range(n)]
d = [[0, 0, 0] for _ in range(n + 1)]
if n == 1:
    print(s[1])
    exit(0)
d[1][1] = s[1]
d[1][2] = 0
d[2][1] = s[2]
d[2][2] = s[1] + s[2]
for i in range(3, n + 1):
    d[i][1] = max(d[i - 2][1], d[i - 2][2]) + s[i]
    d[i][2] = d[i - 1][1] + s[i]
print(max(d[n][1], d[n][2]))
```

```python
n = int(input())
s = [0] + [int(input()) for _ in range(n)]
tot = sum(s)
if n <= 2:
    print(tot)
else:
    d = [0] * (n + 1)
    d[1] = s[1]
    d[2] = s[2]
    d[3] = s[3]
    for i in range(4, n):
        d[i] = min(d[i - 2], d[i - 3]) + s[i]
    print(tot - min(d[n - 1], d[n - 2]))
```

```python
n = int(input())
score = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n + 1)
if n >= 1:
    dp[1] = score[1]
if n >= 2:
    dp[2] = score[1] + score[2]
for i in range(3, n + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + score[i - 1]) + score[i]
print(dp[n])
```

```java
import java.io.*;

public class Main {
    static int[] s = new int[305];
    static int[][] d = new int[305][3];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 1; i <= n; i++) {
            s[i] = Integer.parseInt(br.readLine());
        }

        if (n == 1) {
            System.out.println(s[1]);
            return;
        }

        d[1][1] = s[1];
        d[1][2] = 0;
        d[2][1] = s[2];
        d[2][2] = s[1] + s[2];

        for (int i = 3; i <= n; i++) {
            d[i][1] = Math.max(d[i - 2][1], d[i - 2][2]) + s[i];
            d[i][2] = d[i - 1][1] + s[i];
        }

        System.out.println(Math.max(d[n][1], d[n][2]));
    }
}
```

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] s = new int[305];
        int[] d = new int[305];
        int tot = 0;

        for (int i = 1; i <= n; i++) {
            s[i] = sc.nextInt();
            tot += s[i];
        }

        if (n <= 2) {
            System.out.println(tot);
            return;
        }

        d[1] = s[1];
        d[2] = s[2];
        d[3] = s[3];

        for (int i = 4; i <= n - 1; i++)
            d[i] = Math.min(d[i - 2], d[i - 3]) + s[i];

        System.out.println(tot - Math.min(d[n - 1], d[n - 2]));
    }
}
```

### BOJ1149: RGB거리

```python
n = int(input())
r = [0] * (n + 1)
g = [0] * (n + 1)
b = [0] * (n + 1)
for i in range(1, n + 1):
    r[i], g[i], b[i] = map(int, input().split())
d = [[0] * 3 for _ in range(n + 1)]
d[1][0] = r[1]
d[1][1] = g[1]
d[1][2] = b[1]
for i in range(2, n + 1):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + r[i]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + g[i]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + b[i]
print(min(d[n]))
```

```python
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0] = cost[0]
for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]
print(min(dp[n - 1]))
```

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] r = new int[n + 1];
        int[] g = new int[n + 1];
        int[] b = new int[n + 1];
        
        for (int i = 1; i <= n; i++) {
            r[i] = sc.nextInt();
            g[i] = sc.nextInt();
            b[i] = sc.nextInt();
        }

        int[][] d = new int[n + 1][3];
        d[1][0] = r[1];
        d[1][1] = g[1];
        d[1][2] = b[1];

        for (int i = 2; i <= n; i++) {
            d[i][0] = Math.min(d[i - 1][1], d[i - 1][2]) + r[i];
            d[i][1] = Math.min(d[i - 1][0], d[i - 1][2]) + g[i];
            d[i][2] = Math.min(d[i - 1][0], d[i - 1][1]) + b[i];
        }

        System.out.println(Math.min(d[n][0], Math.min(d[n][1], d[n][2])));
    }
}
```

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] cost = new int[n][3];
        int[][] dp = new int[n][3];

        for (int i = 0; i < n; i++) {
            cost[i][0] = sc.nextInt();
            cost[i][1] = sc.nextInt();
            cost[i][2] = sc.nextInt();
        }

        dp[0][0] = cost[0][0];
        dp[0][1] = cost[0][1];
        dp[0][2] = cost[0][2];

        for (int i = 1; i < n; i++) {
            dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0];
            dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1];
            dp[i][2] = Math.min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2];
        }

        System.out.println(Math.min(dp[n - 1][0], Math.min(dp[n - 1][1], dp[n - 1][2])));
    }
}
```

### BOJ11726: 2×n 타일링

```python
n = int(input())
d = [0] * (n + 2)
d[1], d[2] = 1, 2
for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2]) % 10007
print(d[n])
```

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int[] d = new int[n + 2];
        
        d[1] = 1;
        d[2] = 2;
        
        for (int i = 3; i <= n; i++) {
            d[i] = (d[i - 1] + d[i - 2]) % 10007;
        }
        
        System.out.println(d[n]);
    }
}
```

### BOJ11659: 구간 합 구하기 4

```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + a[i - 1]
for _ in range(m):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i - 1])
```

```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] a = new int[n + 1];
        int[] prefix = new int[n + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
            prefix[i] = prefix[i - 1] + a[i];
        }

        StringBuilder sb = new StringBuilder();
        for (int t = 0; t < m; t++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            sb.append(prefix[j] - prefix[i - 1]).append("\n");
        }

        System.out.print(sb);
    }
}
```

### BOJ12852: 1로 만들기 2

```python
n = int(input())
d = [0] * (n + 1)
pre = [0] * (n + 1)
for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    pre[i] = i - 1
    if i % 2 == 0 and d[i] > d[i // 2] + 1:
        d[i] = d[i // 2] + 1
        pre[i] = i // 2
    if i % 3 == 0 and d[i] > d[i // 3] + 1:
        d[i] = d[i // 3] + 1
        pre[i] = i // 3
print(d[n])
cur = n
while True:
    print(cur, end=' ')
    if cur == 1:
        break
    cur = pre[cur]
```

```java
import java.io.*;

public class Main {
    static int[] d = new int[1000001];
    static int[] pre = new int[1000001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        d[1] = 0;
        for (int i = 2; i <= n; i++) {
            d[i] = d[i - 1] + 1;
            pre[i] = i - 1;
            if (i % 2 == 0 && d[i] > d[i / 2] + 1) {
                d[i] = d[i / 2] + 1;
                pre[i] = i / 2;
            }
            if (i % 3 == 0 && d[i] > d[i / 3] + 1) {
                d[i] = d[i / 3] + 1;
                pre[i] = i / 3;
            }
        }

        System.out.println(d[n]);
        StringBuilder sb = new StringBuilder();
        int cur = n;
        while (true) {
            sb.append(cur).append(" ");
            if (cur == 1) break;
            cur = pre[cur];
        }
        System.out.println(sb.toString());
    }
}
```

### BOJ9251: LCS

```python
a = input().strip()
b = input().strip()
n = len(a)
m = len(b)
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[n][m])
```

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String a = br.readLine();
        String b = br.readLine();

        int n = a.length();
        int m = b.length();

        int[][] dp = new int[n + 1][m + 1];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (a.charAt(i - 1) == b.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1] + 1;
                else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }

        System.out.println(dp[n][m]);
    }
}
```

### BOJ9084: 동전

```python
T = int(input())
for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [[0] * (m + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for i in range(n):
        for j in range(1, m + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j - coins[i] >= 0:
                dp[i][j] += dp[i][j - coins[i]]
    print(dp[n - 1][m])
```

```python
T = int(input())
for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0] * (m + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, m + 1):
            dp[j] += dp[j - coin]
    print(dp[m])
```

```java
import java.io.*;
import java.util.*;

public class Main {
    static int[][] dp = new int[22][10002];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            for (int[] row : dp)
                Arrays.fill(row, 0);

            int n = Integer.parseInt(br.readLine());
            int[] coins = new int[n];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                coins[i] = Integer.parseInt(st.nextToken());
                dp[i][0] = 1;
            }

            int m = Integer.parseInt(br.readLine());

            for (int i = 0; i < n; i++) {
                for (int j = 1; j <= m; j++) {
                    if (i > 0) dp[i][j] += dp[i - 1][j];
                    if (j - coins[i] >= 0) dp[i][j] += dp[i][j - coins[i]];
                }
            }

            System.out.println(dp[n - 1][m]);
        }
    }
}
```

### BOJ12865: 평범한 배낭

```python
n, k = map(int, input().split())
w = []
v = []
for _ in range(n):
    wi, vi = map(int, input().split())
    w.append(wi)
    v.append(vi)
dp = [[0] * (k + 1) for _ in range(n)]
for i in range(n):
    for j in range(1, k + 1):
        if i > 0:
            dp[i][j] = dp[i - 1][j]
        if j - w[i] >= 0:
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i])
            else:
                dp[i][j] = v[i]
print(dp[n - 1][k])
```

```python
n, k = map(int, input().split())
dp = [0] * (k + 1)
for _ in range(n):
    w, v = map(int, input().split())
    for j in range(k, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)
print(dp[k])
```

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int[] w = new int[n];
        int[] v = new int[n];
        int[][] dp = new int[n][k + 1];

        for (int i = 0; i < n; i++) {
            w[i] = sc.nextInt();
            v[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                if (i > 0) dp[i][j] = dp[i - 1][j];
                if (j - w[i] >= 0) {
                    if (i > 0) dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - w[i]] + v[i]);
                    else dp[i][j] = v[i];
                }
            }
        }

        System.out.println(dp[n - 1][k]);
    }
}
```

### BOJ1915: 가장 큰 정사각형

```python
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
dp = [[0] * m for _ in range(n)]
for i in range(n):
    dp[i][0] = int(board[i][0])
for j in range(m):
    dp[0][j] = int(board[0][j])
for i in range(1, n):
    for j in range(1, m):
        if board[i][j] == '1':
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
ans = max(max(row) for row in dp)
print(ans * ans)
```

```python
n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            ans = max(ans, dp[i][j])
print(ans * ans)
```

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine();

        String[] board = new String[n];
        for (int i = 0; i < n; i++) {
            board[i] = sc.nextLine();
        }

        int[][] dp = new int[n][m];
        int maxLen = 0;

        for (int i = 0; i < n; i++)
            dp[i][0] = board[i].charAt(0) - '0';
        for (int j = 0; j < m; j++)
            dp[0][j] = board[0].charAt(j) - '0';

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (board[i].charAt(j) == '1') {
                    dp[i][j] = Math.min(Math.min(dp[i - 1][j], dp[i - 1][j - 1]), dp[i][j - 1]) + 1;
                }
            }
        }

        for (int[] row : dp) {
            for (int val : row)
                maxLen = Math.max(maxLen, val);
        }

        System.out.println(maxLen * maxLen);
    }
}
```

### BOJ1351: 무한 수열

```python
import sys

sys.setrecursionlimit(10 ** 6)

n, p, q = map(int, input().split())
memo = {}

def solve(x):
    if x == 0:
        return 1
    if x in memo:
        return memo[x]
    memo[x] = solve(x // p) + solve(x // q)
    return memo[x]

print(solve(n))
```

```java
import java.util.*;
import java.io.*;

public class Main {
    static long n, p, q;
    static Map<Long, Long> memo = new HashMap<>();

    public static long solve(long x) {
        if (x == 0) return 1;
        if (memo.containsKey(x)) return memo.get(x);
        long val = solve(x / p) + solve(x / q);
        memo.put(x, val);
        return val;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] parts = br.readLine().split(" ");
        n = Long.parseLong(parts[0]);
        p = Long.parseLong(parts[1]);
        q = Long.parseLong(parts[2]);
        System.out.println(solve(n));
    }
}
```

### BOJ1937: 욕심쟁이 판다

```python
import sys

sys.setrecursionlimit(1000000)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def check(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

def solve(x, y):
    if d[x][y] != -1:
        return d[x][y]
    d[x][y] = 1
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if check(nx, ny) or board[x][y] >= board[nx][ny]:
            continue
        d[x][y] = max(d[x][y], solve(nx, ny) + 1)
    return d[x][y]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, solve(i, j))
print(ans)
```

```java
import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int[][] board;
    static int[][] d;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    static boolean check(int x, int y) {
        return x < 0 || x >= n || y < 0 || y >= n;
    }

    static int solve(int x, int y) {
        if (d[x][y] != -1) return d[x][y];
        d[x][y] = 1;
        for (int dir = 0; dir < 4; dir++) {
            int nx = x + dx[dir], ny = y + dy[dir];
            if (check(nx, ny) || board[x][y] >= board[nx][ny]) continue;
            d[x][y] = Math.max(d[x][y], solve(nx, ny) + 1);
        }
        return d[x][y];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        board = new int[n][n];
        d = new int[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                d[i][j] = -1;
            }
        }

        int max = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                max = Math.max(max, solve(i, j));

        System.out.println(max);
    }
}
```

### BOJ1949: 우수 마을

```python
import sys

sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)
d1 = [0] * (n + 1)
d2 = [0] * (n + 1)

def dfs(cur, par):
    d1[cur] = a[cur]
    d2[cur] = 0
    for nxt in adj[cur]:
        if nxt == par:
            continue
        dfs(nxt, cur)
        d1[cur] += d2[nxt]
        d2[cur] += max(d1[nxt], d2[nxt])

dfs(1, 0)
print(max(d1[1], d2[1]))
```

```java
import java.util.*;

public class Main {
    static int n;
    static int[] a = new int[10005];
    static int[] d1 = new int[10005];
    static int[] d2 = new int[10005];
    static List<Integer>[] adj = new ArrayList[10005];

    public static void dfs(int cur, int par) {
        d1[cur] = a[cur];
        d2[cur] = 0;
        for (int nxt : adj[cur]) {
            if (nxt == par) continue;
            dfs(nxt, cur);
            d1[cur] += d2[nxt];
            d2[cur] += Math.max(d1[nxt], d2[nxt]);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            a[i] = sc.nextInt();
            adj[i] = new ArrayList<>();
        }
        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v);
            adj[v].add(u);
        }
        dfs(1, 0);
        System.out.println(Math.max(d1[1], d2[1]));
    }
}
```

### BOJ1005: ACM Craft

```python
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    adj = [[] for _ in range(n + 1)]
    d = [-1] * (n + 1)
    for _ in range(k):
        u, v = map(int, input().split())
        adj[v].append(u)
    w = int(input())

    def solve(x):
        if d[x] != -1:
            return d[x]
        d[x] = 0
        for nxt in adj[x]:
            d[x] = max(d[x], solve(nxt))
        d[x] += a[x]
        return d[x]

    print(solve(w))
```

```java
import java.util.*;

public class Main {
    static int n, k, w;
    static int[] a = new int[1005];
    static int[] d = new int[1005];
    static List<Integer>[] adj = new ArrayList[1005];

    static int go(int x) {
        if (d[x] != -1) return d[x];
        d[x] = 0;
        for (int nxt : adj[x])
            d[x] = Math.max(d[x], go(nxt));
        d[x] += a[x];
        return d[x];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            n = sc.nextInt();
            k = sc.nextInt();
            for (int i = 1; i <= n; i++) {
                a[i] = sc.nextInt();
                adj[i] = new ArrayList<>();
                d[i] = -1;
            }

            for (int i = 0; i < k; i++) {
                int u = sc.nextInt(), v = sc.nextInt();
                adj[v].add(u);
            }

            w = sc.nextInt();
            System.out.println(go(w));
        }
    }
}
```