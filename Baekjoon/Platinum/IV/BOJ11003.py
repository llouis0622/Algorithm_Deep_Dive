from collections import deque

N, L = map(int, input().split())
now = list(map(int, input().split()))
deq = deque()

for i in range(N):
    while deq and deq[-1][0] > now[i]:
        deq.pop()
    deq.append((now[i], i))

    if deq[0][1] <= i - L:
        deq.popleft()

    print(deq[0][0], end=' ')