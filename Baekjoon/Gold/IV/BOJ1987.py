import sys

r, c = map(int, sys.stdin.readline().split())
temp = [[ord(ch) - 65 for ch in sys.stdin.readline().strip()] for _ in range(r)]
check = 0
for i in range(r):
    for j in range(c):
        check |= 1 << temp[i][j]
num = check.bit_count()
dir = ((1, 0), (-1, 0), (0, 1), (0, -1))
ans = 1
s = [(0, 0, 1 << temp[0][0], 1)]
while s:
    x, y, cur, d = s.pop()
    if d > ans:
        ans = d
    if ans == num:
        print(ans)
        sys.exit(0)
    if d + (num - cur.bit_count()) <= ans:
        continue
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            idx = 1 << temp[nx][ny]
            if (cur & idx) == 0:
                s.append((nx, ny, cur | idx, d + 1))
print(ans)