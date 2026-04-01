from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
dq = deque(range(1, N + 1))
arr = []
while dq:
    dq.rotate(-(K - 1))
    arr.append(dq.popleft())
print('<' + ', '.join(map(str, arr)) + '>')
