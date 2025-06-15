from collections import deque

R, C = map(int, input().split())
pos = [list(map(int, input().split())) for _ in range(R)]
N = int(input())
temp = [tuple(map(int, input().split())) for _ in range(N)]
check = [[-1] * C for _ in range(R)]
q = deque()
for c in range(C):
    if pos[0][c] == 1:
        check[0][c] = 0
        q.append((0, c))
while q:
    x, y = q.popleft()
    for dx, dy in temp:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if pos[nx][ny] == 1 and check[nx][ny] == -1:
                check[nx][ny] = check[x][y] + 1
                q.append((nx, ny))
ans = -1
for c in range(C):
    if check[R - 1][c] != -1:
        if ans == -1 or check[R - 1][c] < ans:
            ans = check[R - 1][c]
print(ans)