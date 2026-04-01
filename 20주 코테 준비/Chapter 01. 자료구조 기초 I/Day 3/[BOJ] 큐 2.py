from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
q = deque()
for _ in range(N):
    op = input().split()

    if op[0] == 'push':
        q.append(int(op[1]))
    elif op[0] == 'pop':
        print(q.popleft() if q else -1)
    elif op[0] == 'size':
        print(len(q))
    elif op[0] == 'empty':
        print(0 if q else 1)
    elif op[0] == 'front':
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)
