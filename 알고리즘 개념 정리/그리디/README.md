## 1️⃣ 그리디(Greedy)

### 그리디란?

- 지금 가장 최적인 답을 근시안적으로 택하는 알고리즘
- 관찰을 통해 탐색 범위를 줄이는 알고리즘

### 이상적인 풀이 흐름

- 관찰을 통해 탐색 범위를 줄이는 방법을 고안
- 탐색 범위를 줄여도 올바른 결과를 낸다는 사실을 수학적으로 증명
- 구현해서 문제를 통과

### 현실적인 풀이 흐름

- 관찰을 통해 탐색 범위를 줄이는 방법을 고안
- 탐색 범위를 줄여도 올바른 결과를 낸다는 강한 믿음을 가짐
- 믿음을 가지고 구현해서 문제를 통과

### 절망적인 풀이 흐름

- 관찰을 통해 탐색 범위를 줄이는 잘못된 방법을 고안
- 탐색 범위를 줄여도 올바른 결과를 낸다는 강한 믿음을 가짐
- 믿음을 가지고 구현했는데 계속 틀림

## 2️⃣ 그리디 풀이 방법

### **코딩 테스트에서의 추천 전략**

- 거의 똑같은 문제를 풀어봤거나 간단한 문제여서 나의 그리디 풀이를 100% 확신한다
    
    → 짜서 제출해보고 틀리면 빠르게 손절
    
- 100% 확신은 없지만 맞는 것 같은 그리디 풀이를 찾았다
    
    → 일단은 넘어가고 문제를 풀게 없거나 종료가 20~40분 남은 시점에 코딩 시작
    

### **그리디 선택 가능성**

- 현재 선택이 이후 선택에 영향을 미치는가? → 영향이 적으면 그리디 가능성 ⬆︎
- 되돌릴 수 없는 선택인가? → 되돌리지 않고 한 번의 선택으로 끝나면 그리디 후보
- 부분 문제의 최적해가 전체 최적해로 이어지는가? → 그리디 & 최적 부분 구조 만족
- 정렬로 풀이 조건을 단순화할 수 있는가? → 정렬 기반 문제라면 그리디 가능성 ⬆︎

### **그리디 문제 판별법**

- 큰 순서/작은 순서로 나눠야 함 : 동전, ATM, 줄 세우기 등
- 빠른 시간/짧은 거리/적은 비용 : 회의실 배정, 배달 동선 등
- 최대/최소 개수/길이 : 최대 회의 수, 최소 이동 거리
- 조건을 만족시키며 최대화/최소화 : DP랑 구별해서 조건이 간단하면 그리디

### **그리디 풀이 기본 흐름**

- 조건 파악 – 문제 조건 중 최대/최소 키워드 주목 & 제약이 단순할수록 그리디 ⬆︎
- 정렬 기준 찾기 – 대부분 정렬이 핵심(시작/끝/크기/비용 등)
- ㅡ메탐욕 조건 증명하기 – 한 번의 선택이 최적임을 납득
대표적인 조건 : 항상 가장 작은 비용부터 선택 → 전역 최적 보장
- 반복문으로 구현 – 보통 정렬 후 한 번의 반복문으로 끝남
- 반례 시뮬레이션 – 선택을 바꿨을 때 더 나은 해가 있는지 꼭 비교

## 3️⃣ 수업 코드

### BOJ11047: 동전 0

```python
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
cnt = 0
for coin in reversed(coins):
    if K >= coin:
        cnt += K // coin
        K %= coin
print(cnt)
```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] coins = new int[n];
        
        for (int i = 0; i < n; i++) {
            coins[i] = sc.nextInt();
        }

        int cnt = 0;
        
        for (int i = n - 1; i >= 0; i--) {
            if (k >= coins[i]) {
                cnt += k / coins[i];
                k %= coins[i];
            }
        }

        System.out.println(cnt);
    }
}
```

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    
    vector<int> coins(n);
    
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    int cnt = 0;

    for (int i = n - 1; i >= 0; i--) {
        if (k >= coins[i]) {
            cnt += k / coins[i];
            k %= coins[i];
        }
    }

    cout << cnt << '\n';

    return 0;
}
```

### BOJ1931: 회의실 배정

```python
n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))
cnt = 0
time = 0
for start, end in meetings:
    if start >= time:
        cnt += 1
        time = end
print(cnt)
```

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int[][] meetings = new int[n][2];
        
        for (int i = 0; i < n; i++) {
            meetings[i][0] = sc.nextInt();
            meetings[i][1] = sc.nextInt();
        }

        Arrays.sort(meetings, (a, b) -> {
            if (a[1] == b[1]) return a[0] - b[0];
            return a[1] - b[1];
        });

        int cnt = 0;
        int time = 0;
        
        for (int[] m : meetings) {
            if (m[0] >= time) {
                cnt++;
                time = m[1];
            }
        }

        System.out.println(cnt);
    }
}
```

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> meetings(n);

    for (int i = 0; i < n; i++) {
        cin >> meetings[i].first >> meetings[i].second;
    }

    sort(meetings.begin(), meetings.end(), [](auto &a, auto &b) {
        if (a.second == b.second) return a.first < b.first;
        return a.second < b.second;
    });

    int cnt = 0, time = 0;
    
    for (auto &m : meetings) {
        if (m.first >= time) {
            cnt++;
            time = m.second;
        }
    }

    cout << cnt << '\n';
    
    return 0;
}
```

### BOJ2217: 로프

```python
N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)
ans = 0
for i in range(N):
    weight = ropes[i] * (i + 1)
    if weight > ans:
        ans = weight
print(ans)
```

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        Integer[] ropes = new Integer[n];

        for (int i = 0; i < n; i++) {
            ropes[i] = sc.nextInt();
        }

        Arrays.sort(ropes, Collections.reverseOrder());

        int ans = 0;
        
        for (int i = 0; i < n; i++) {
            int weight = ropes[i] * (i + 1);
            
            if (weight > ans) {
                ans = weight;
            }
        }

        System.out.println(ans);
    }
}
```

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> ropes(n);

    for (int i = 0; i < n; i++) {
        cin >> ropes[i];
    }

    sort(ropes.rbegin(), ropes.rend());

    int ans = 0;

    for (int i = 0; i < n; i++) {
        int weight = ropes[i] * (i + 1);

        if (weight > ans) {
            ans = weight;
        }
    }

    cout << ans << '\n';

    return 0;
}
```

### BOJ1026: 보물

```python
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
ans = sum(a * b for a, b in zip(A, B))
print(ans)
```

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int[] A = new int[n];
        Integer[] B = new Integer[n];

        for (int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            B[i] = sc.nextInt();
        }

        Arrays.sort(A);
        Arrays.sort(B, Collections.reverseOrder());

        int ans = 0;
        
        for (int i = 0; i < n; i++) {
            ans += A[i] * B[i];
        }

        System.out.println(ans);
    }
}
```

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> A(n), B(n);

    for (int i = 0; i < n; i++) cin >> A[i];
    for (int i = 0; i < n; i++) cin >> B[i];

    sort(A.begin(), A.end());
    sort(B.rbegin(), B.rend());

    int ans = 0;

    for (int i = 0; i < n; i++) {
        ans += A[i] * B[i];
    }

    cout << ans << '\n';

    return 0;
}
```