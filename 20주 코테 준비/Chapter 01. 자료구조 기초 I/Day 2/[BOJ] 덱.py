from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
dq = deque()
for _ in range(N):
    op = input().split()

    if op[0] == 'push_front':
        dq.appendleft(int(op[1]))
    elif op[0] == 'push_back':
        dq.append(int(op[1]))
    elif op[0] == 'pop_front':
        print(dq.popleft() if dq else -1)
    elif op[0] == 'pop_back':
        print(dq.pop() if dq else -1)
    elif op[0] == 'size':
        print(len(dq))
    elif op[0] == 'empty':
        print(0 if dq else 1)
    elif op[0] == 'front':
        print(dq[0] if dq else -1)
    else:
        print(dq[-1] if dq else -1)
