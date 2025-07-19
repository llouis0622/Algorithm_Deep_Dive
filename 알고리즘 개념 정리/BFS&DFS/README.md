## 1️⃣ BFS/DFS

### BFS

- 다차원 배열에서 각 칸을 방문할 때 너비를 우선으로 방문하는 알고리즘

### BFS 순회 방법

- 시작하는 칸을 큐에 넣고 방문했다는 표시를 남김
- 큐에서 원소를 꺼내어 그 칸에 상하좌우로 인접한 칸에 대해 3번 진행
- 해당 칸을 이전에 방문했다면 아무 것도 하지 않고, 처음으로 방문했다면 방문했다는 표시를 남기고 해당 칸을 큐에 삽입
- 큐가 빌 때까지 2번을 반복

### DFS

- 다차원 배열에서 각 칸을 방문할 때 깊이를 우선으로 방문하는 알고리즘

### DFS 순회 방법

- 시작하는 칸을 스택에 넣고 방문했다는 표시를 남김
- 스택에서 원소를 꺼내어 그 칸에 상하좌우로 인접한 칸에 대해 3번 진행
- 해당 칸을 이전에 방문했다면 아무 것도 하지 않고, 처음으로 방문했다면 방문했다는 표시를 남기고 해당 칸을 스택에 삽입
- 스택이 빌 때까지 2번을 반복

## 2️⃣ BFS/DFS 풀이 방법

### BFS **선택 가능성**

- 가장 적은 횟수로 갈 수 있는가
- 한 칸씩 퍼져나가는 상황인가
- 동시에 여러 곳에서 퍼지는가
- 맵/그래프가 주어지고 이동/확산/최소 거리인가
- 방문 순서가 중요한가

### BFS **문제 판별법**

- 최단 거리/최소 단계 문제 → 100% BFS
- 격자형 이동(미로, 맵) → BFS가 안정적
- 레벨별 탐색이 필요 → BFS가 유리
- 그래프에서 모든 노드까지의 최소 거리 필요 → BFS
- DFS로 하면 깊이가 너무 깊어질 때 → BFS로 안전하게
- 방문 순서가 단계별로 필요한 경우 → BFS

### BFS **풀이 기본 흐름**

- 시작점 큐에 넣고 방문 표시 - q.append(start) + visited[start] = True
- 큐가 빌 때까지 반복 - while queue:
- 큐에서 현재 노드 꺼내기 - node = queue.popleft()
- 인접 노드 확인 - 조건에 맞고 미방문이면 큐에 넣기
- 거리/단계 갱신 - 필요하다면 거리 배열로 따로 관리

### BFS 필수 요소

- 큐 : FIFO 구조 유지
- 방문 배열 : 중복 방문 방지
- dx/dy : 격자형 이동
- 거리 배열 : 최단 거리 문제라면 반드시
- 다중 시작점 : 바이러스/불 등 동시 확산

### DFS **선택 가능성**

- 모든 경로를 다 확인해야 하는가
- 조건이 틀리면 바로 가지치기가 필요한가
- 트리 구조인가
- 반복문으로 풀기 어렵고 계층적으로 쌓이는가

### DFS **문제 판별법**

- 모든 경우의 수를 다 탐색해야 함 → 100% DFS
- 경로/분기/순열/조합 → DFS 적합
- 백트래킹 문제 → DFS 기반
- 트리 구조 순회 → DFS 적합
- 그래프 연결 요소 찾기 → DFS/BFS 모두 가능
- 깊게 들어가서 중간에 조건 확인 & 돌아오기 → DFS만 가능

### DFS **풀이 기본 흐름**

- 현재 노드 방문 처리 - visited 표시
- 조건 만족 여부 확인 - 중간에 틀리면 return
- 인접 노드로 이동 - 재귀 or 스택 사용
- 모든 경로 끝까지 간 뒤 돌아옴 - 백트래킹 포함 가능

### DFS 필수 요소

- visited 리스트 꼭 사용 : 중복 방문 방지
- 재귀 깊이 주의 : sys.setrecursionlimit()
- 백트래킹은 DFS의 확장 : 조건 불만족 시 return
- 중간 출력으로 흐름 디버깅 : 스택 흐름 시각화
- 격자형은 dx/dy로 이동 : 상하좌우 이동

## 3️⃣ 수업 코드

### BOJ1926: 그림

```python
from collections import deque

n, m = map(int, input().split())  # 세로 크기 n, 가로 크기 m
board = [list(map(int, input().split())) for _ in range(n)]  # 그림 정보 입력
visited = [[False] * m for _ in range(n)]  # 방문 여부
dx = [1, 0, -1, 0]  # 상하좌우 이동 배열
dy = [0, 1, 0, -1]
num = 0  # 그림의 개수
size = 0  # 가장 큰 그림의 넓이
for i in range(n):
    for j in range(m):
        # 이미 방문했거나 색칠되지 않은 칸이면 건너뜀
        if visited[i][j] or board[i][j] == 0:
            continue
        num += 1  # 새로운 그림 발견 시 개수 증가
        q = deque()
        visited[i][j] = True  # 방문 처리
        q.append((i, j))
        temp = 1  # 현재 그림 넓이
        # BFS 탐색 시작
        while q:
            x, y = q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                # 범위 밖이면 건너뜀
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                # 이미 방문했거나 색칠되지 않았다면 건너뜀
                if visited[nx][ny] or board[nx][ny] == 0:
                    continue
                visited[nx][ny] = True  # 방문 처리
                q.append((nx, ny))
                temp += 1  # 그림 넓이 증가
        size = max(size, temp)  # 최대 넓이 갱신
print(num)  # 그림의 개수 출력
print(size)  # 가장 큰 그림의 넓이 출력
```

```java
import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static int[][] board;
    static boolean[][] visited;

    static int[] dx = {1, 0, -1, 0}; // 상하좌우
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int num = 0;   // 그림의 개수
        int size = 0;  // 가장 큰 그림의 넓이

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visited[i][j] || board[i][j] == 0) continue;

                num++; // 새로운 그림 발견
                int temp = 1; // 현재 그림 넓이
                Queue<int[]> q = new LinkedList<>();
                visited[i][j] = true;
                q.offer(new int[]{i, j});

                while (!q.isEmpty()) {
                    int[] cur = q.poll();
                    int x = cur[0];
                    int y = cur[1];

                    for (int dir = 0; dir < 4; dir++) {
                        int nx = x + dx[dir];
                        int ny = y + dy[dir];

                        if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                        if (visited[nx][ny] || board[nx][ny] == 0) continue;

                        visited[nx][ny] = true;
                        q.offer(new int[]{nx, ny});
                        temp++;
                    }
                }
                size = Math.max(size, temp); // 최대 넓이 갱신
            }
        }

        System.out.println(num);
        System.out.println(size);
    }
}
```

### BOJ2178: 미로 탐색

```python
from collections import deque

n, m = map(int, input().split())  # 세로, 가로 크기
board = [list(map(int, input().strip())) for _ in range(n)]  # 붙어서 들어오는 미로 정보
visited = [[False] * m for _ in range(n)]  # 방문 여부
dx = [1, 0, -1, 0]  # 상하좌우
dy = [0, 1, 0, -1]
q = deque()
q.append((0, 0))  # 시작점 (0, 0) 삽입
visited[0][0] = True
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 밖이면 패스
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 방문했거나 벽이면 패스
        if visited[nx][ny] or board[nx][ny] == 0:
            continue
        # 방문 처리하고 거리 갱신
        visited[nx][ny] = True
        board[nx][ny] = board[x][y] + 1  # 시작칸 포함 → 현재 칸까지 거리 +1
        q.append((nx, ny))
# 도착칸에 저장된 값이 최소 칸 수
print(board[n - 1][m - 1])
```

```java
import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static int[][] board;
    static boolean[][] visited;
    static int[] dx = {1, 0, -1, 0}; // 상하좌우
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine().trim();
            for (int j = 0; j < m; j++) {
                board[i][j] = line.charAt(j) - '0';
            }
        }

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0});
        visited[0][0] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];

            for (int dir = 0; dir < 4; dir++) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                // 범위 체크
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                // 방문했거나 벽이면 패스
                if (visited[nx][ny] || board[nx][ny] == 0) continue;

                visited[nx][ny] = true;
                board[nx][ny] = board[x][y] + 1; // 거리 누적
                q.offer(new int[]{nx, ny});
            }
        }

        System.out.println(board[n - 1][m - 1]);
    }
}
```

### BOJ7576: 토마토

```python
from collections import deque

m, n = map(int, input().split())  # m: 가로 칸 수, n: 세로 칸 수
board = [list(map(int, input().split())) for _ in range(n)]  # 상자 정보
q = deque()
dx = [1, 0, -1, 0]  # 상하좌우
dy = [0, 1, 0, -1]
# 시작: 익은 토마토(1) 전부 큐에 삽입
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))
# BFS 시작
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위를 벗어나면 무시
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 이미 익었거나 빈 칸(-1)이라면 무시
        if board[nx][ny] != 0:
            continue
        # 안 익은 토마토(0)이면 익히고 큐에 넣기
        board[nx][ny] = board[x][y] + 1  # 현재 칸 값 +1 = 익은 날짜
        q.append((nx, ny))
ans = 0  # 결과: 최소 일수
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:  # 안 익은 토마토가 있으면
            print(-1)
            exit(0)
        ans = max(ans, board[i][j])  # 최댓값 갱신
print(ans - 1)  # 시작점이 1부터 시작했으므로 -1
```

```java
import java.util.*;
import java.io.*;

public class Main {
    static int m, n;
    static int[][] board;
    static int[] dx = {1, 0, -1, 0};  // 상하좌우
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken()); // 가로
        n = Integer.parseInt(st.nextToken()); // 세로

        board = new int[n][m];
        Queue<int[]> q = new LinkedList<>();

        // 보드 입력 + 익은 토마토(1) 전부 큐에 삽입
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 1) {
                    q.offer(new int[]{i, j});
                }
            }
        }

        // BFS
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];

            for (int dir = 0; dir < 4; dir++) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                if (board[nx][ny] != 0) continue;

                board[nx][ny] = board[x][y] + 1;
                q.offer(new int[]{nx, ny});
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 0) {
                    System.out.println(-1);
                    return;
                }
                ans = Math.max(ans, board[i][j]);
            }
        }

        System.out.println(ans - 1);
    }
}
```

### BOJ4179: 불!

```python
from collections import deque

r, c = map(int, input().split())  # 행, 열 입력
board = [list(input().strip()) for _ in range(r)]  # 미로 정보
fire = [[-1] * c for _ in range(r)]  # 불의 도착 시간
jihun = [[-1] * c for _ in range(r)]  # 지훈이의 도착 시간
q1 = deque()  # 불 BFS 큐
q2 = deque()  # 지훈이 BFS 큐
# 시작 위치 설정
for i in range(r):
    for j in range(c):
        if board[i][j] == 'F':
            q1.append((i, j))
            fire[i][j] = 0  # 불의 시작점 시간 0
        if board[i][j] == 'J':
            q2.append((i, j))
            jihun[i][j] = 0  # 지훈이의 시작점 시간 0
dx = [1, 0, -1, 0]  # 상하좌우
dy = [0, 1, 0, -1]
# 불 BFS 먼저 돌려서 각 칸까지 도달 시간 계산
while q1:
    x, y = q1.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if board[nx][ny] == '#' or fire[nx][ny] >= 0:
            continue
        fire[nx][ny] = fire[x][y] + 1
        q1.append((nx, ny))
# 지훈이 BFS
while q2:
    x, y = q2.popleft()
    # 가장자리에 닿으면 즉시 탈출 성공
    if x == 0 or y == 0 or x == r - 1 or y == c - 1:
        print(jihun[x][y] + 1)
        exit(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if board[nx][ny] == '#' or jihun[nx][ny] >= 0:
            continue
        # 불보다 빨리 도착할 수 없으면 이동 불가
        if fire[nx][ny] != -1 and fire[nx][ny] <= jihun[x][y] + 1:
            continue
        jihun[nx][ny] = jihun[x][y] + 1
        q2.append((nx, ny))
# 끝까지 탈출 실패
print("IMPOSSIBLE")
```

```java
import java.util.*;
import java.io.*;

public class Main {
    static int r, c;
    static char[][] board;
    static int[][] fire;
    static int[][] jihun;

    static int[] dx = {1, 0, -1, 0}; // 상하좌우
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        board = new char[r][c];
        fire = new int[r][c];
        jihun = new int[r][c];

        for (int i = 0; i < r; i++) {
            String line = br.readLine().trim();
            for (int j = 0; j < c; j++) {
                board[i][j] = line.charAt(j);
                fire[i][j] = -1;  // 불 도착 시간 초기화
                jihun[i][j] = -1; // 지훈이 도착 시간 초기화
            }
        }

        Queue<int[]> q1 = new LinkedList<>(); // 불
        Queue<int[]> q2 = new LinkedList<>(); // 지훈이

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (board[i][j] == 'F') {
                    q1.offer(new int[]{i, j});
                    fire[i][j] = 0;
                }
                if (board[i][j] == 'J') {
                    q2.offer(new int[]{i, j});
                    jihun[i][j] = 0;
                }
            }
        }

        // 불 BFS
        while (!q1.isEmpty()) {
            int[] cur = q1.poll();
            int x = cur[0], y = cur[1];

            for (int dir = 0; dir < 4; dir++) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (nx < 0 || ny < 0 || nx >= r || ny >= c) continue;
                if (board[nx][ny] == '#' || fire[nx][ny] >= 0) continue;

                fire[nx][ny] = fire[x][y] + 1;
                q1.offer(new int[]{nx, ny});
            }
        }

        // 지훈이 BFS
        while (!q2.isEmpty()) {
            int[] cur = q2.poll();
            int x = cur[0], y = cur[1];

            // 가장자리에 닿으면 즉시 탈출
            if (x == 0 || y == 0 || x == r - 1 || y == c - 1) {
                System.out.println(jihun[x][y] + 1);
                return;
            }

            for (int dir = 0; dir < 4; dir++) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (nx < 0 || ny < 0 || nx >= r || ny >= c) continue;
                if (board[nx][ny] == '#' || jihun[nx][ny] >= 0) continue;

                if (fire[nx][ny] != -1 && fire[nx][ny] <= jihun[x][y] + 1) continue;

                jihun[nx][ny] = jihun[x][y] + 1;
                q2.offer(new int[]{nx, ny});
            }
        }

        System.out.println("IMPOSSIBLE");
    }
}
```

### BOJ1697: 숨바꼭질

```python
from collections import deque

n, k = map(int, input().split())  # 수빈이 위치 N, 동생 위치 K 입력
MAX = 100001  # 좌표 최대 범위
dist = [-1] * MAX  # 방문 여부 및 최소 시간 기록용 배열
q = deque()
q.append(n)  # 시작점 삽입
dist[n] = 0  # 시작점 시간은 0초
while q:
    cur = q.popleft()
    if cur == k:
        print(dist[cur])  # 동생 위치 도착 시 최소 시간 출력
        break
    # 3가지 이동: X-1, X+1, 2*X
    for nx in (cur - 1, cur + 1, cur * 2):
        # 범위 안이고, 아직 방문하지 않은 곳이면
        if 0 <= nx < MAX and dist[nx] == -1:
            dist[nx] = dist[cur] + 1  # 현재까지 시간 +1
            q.append(nx)  # 큐에 삽입
```

```java
import java.util.*;
import java.io.*;

public class Main {
    static final int MAX = 100001;
    static int[] dist = new int[MAX];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 수빈이 위치
        int k = Integer.parseInt(st.nextToken()); // 동생 위치

        Arrays.fill(dist, -1); // 방문 여부 -1로 초기화

        Queue<Integer> q = new LinkedList<>();
        q.offer(n);
        dist[n] = 0; // 시작 위치 시간 0초

        while (!q.isEmpty()) {
            int cur = q.poll();

            if (cur == k) {
                System.out.println(dist[cur]);
                break;
            }

            for (int next : new int[]{cur - 1, cur + 1, cur * 2}) {
                if (next < 0 || next >= MAX) continue;
                if (dist[next] != -1) continue;

                dist[next] = dist[cur] + 1; // 현재 위치 시간 +1
                q.offer(next);
            }
        }
    }
}
```