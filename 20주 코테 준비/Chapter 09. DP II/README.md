### DP 심화 - LCS, LIS, 편집거리

- LCS : s1[i] == s2[j]이면 dp[i][j] = dp[i - 1][j - 1] + 1 or max(위, 왼쪽)
- LIS : O(N^2) DP 또는 O(N log N) 이분탐색
  - bisect_left -> 엄격 증가
  - bisect_right -> 비감소
- 편집거리 : 삽입/삭제/교체 최소 연산 수

```python
import bisect


def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def lis(arr):
    tails = []
    for i in arr:
        pos = bisect.bisect_left(tails, i)
        if pos == len(tails):
            tails.append(i)
        else:
            tails[pos] = i
    return len(tails)
```