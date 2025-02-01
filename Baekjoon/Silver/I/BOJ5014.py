from collections import deque

F, S, G, U, D = map(int, input().split())
q = deque([S])
v = [-1] * (F + 1)
v[S] = 0
while q:
    cur = q.popleft()
    if cur == G:
        print(v[cur])
        exit()
    for nxt in (cur + U, cur - D):
        if 1 <= nxt <= F and v[nxt] == -1:
            v[nxt] = v[cur] + 1
            q.append(nxt)
print("use the stairs")