from collections import deque

for _ in range(10):
    T = int(input())
    q = deque(map(int, input().split()))
    num = 1
    while True:
        temp = q.popleft() - num
        if temp <= 0:
            q.append(0)
            break
        q.append(temp)
        num += 1
        if num == 6:
            num = 1
    print(f'#{T}', *q)
