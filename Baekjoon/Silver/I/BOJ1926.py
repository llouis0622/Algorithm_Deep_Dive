from collections import deque


def bfs(lst, x, y, n, m):
    queue = deque([(x, y)])
    lst[x][y] = 0
    area = 1
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and lst[nx][ny] == 1:
                queue.append((nx, ny))
                lst[nx][ny] = 0
                area += 1
    return area


def picture(n, m, lst):
    cnt = 0
    num = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 1:
                cnt += 1
                num = max(num, bfs(lst, i, j, n, m))
    return cnt, num


n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
cnt, num = picture(n, m, lst)
print(cnt)
print(num)