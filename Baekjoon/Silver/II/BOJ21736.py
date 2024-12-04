import sys

N, M = map(int, input().split())
campus = sys.stdin.read().splitlines()


def locate():
    for x in range(N):
        for y in range(M):
            if campus[x][y] == 'I':
                return (x, y)


move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
stack = [locate()]
visited = [[True] * M for _ in range(N)]
count = 0

while stack:
    dx, dy = stack.pop()
    for mx, my in move:
        x, y = dx + mx, dy + my
        if 0 <= x < N and 0 <= y < M and campus[x][y] != 'X' and visited[x][y]:
            stack.append((x, y))
            visited[x][y] = False
            if campus[x][y] == 'P':
                count += 1

print(count if count else 'TT')