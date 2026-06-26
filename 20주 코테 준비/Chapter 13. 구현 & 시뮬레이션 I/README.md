### 구현 & 시뮬레이션 I

- 문제에서 시키는 대로 정확하게 구현하는 능력
- 격자 이동 패턴 : dx = [-1, 0, 1, -], dy = [0, 1, 0, -1]
- 8방향 : dx8 = [-1, -1, -1, 0, 0, 1, 1, 1], dy8 = [-1, 0, 1, -1, 1, -1, 0, 1]
- 시계 방향 회전 : d = (d + 1) % 4
- 반시계 방향 회전 : d = (d - 1) % 4

```python
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def in_bound(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def rotate90(matrix):
    n = len(matrix)
    return [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]
```