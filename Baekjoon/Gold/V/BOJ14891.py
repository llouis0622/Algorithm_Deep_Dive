from collections import deque
import sys

input = sys.stdin.readline

g = [deque(map(int, list(input().strip()))) for _ in range(4)]
k = int(input().strip())
for _ in range(k):
    idx, d = map(int, input().split())
    idx -= 1
    num = [0, 0, 0, 0]
    num[idx] = d
    for i in range(idx, 0, -1):
        if g[i][6] != g[i - 1][2]:
            num[i - 1] = -num[i]
        else:
            break
    for i in range(idx, 3):
        if g[i][2] != g[i + 1][6]:
            num[i + 1] = -num[i]
        else:
            break
    for i in range(4):
        if num[i] == 1:
            g[i].appendleft(g[i].pop())
        elif num[i] == -1:
            g[i].append(g[i].popleft())
ans = 0
for i in range(4):
    if g[i][0] == 1:
        ans += 1 << i
print(ans)