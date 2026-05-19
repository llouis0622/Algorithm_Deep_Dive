### DP 기초 - 1D

- DP 풀이 순서 : DP[i] 정의 -> 점화식 -> base case -> 구현
- 메모이제이션(Top-down) : 재귀 + lru_cache
- 타뷸레이션(Bottom-up) : 반복문으로 테이블 채우기
- 대표 패턴 : 피보나치, 계단 오르기, 0-1 배낭 문제, 동전 교환

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def stair(a):
    n = len(a)
    dp = [0] * n
    dp[0], dp[1] = a[0], a[0] + a[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + a[i])
    return dp[n - 1]


def knapsack(w, wt, val):
    dp = [0] * (w + 1)
    for i in range(len(wt)):
        for j in range(w, wt[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - wt[i]] + val[i])
    return dp[w]
```