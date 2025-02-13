import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
video = [list(map(int, line)) for line in data[1:N + 1]]


def check(x, y, size):
    temp = video[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if video[i][j] != temp:
                return False
    return True


def quadtree(x, y, size):
    if check(x, y, size):
        return str(video[x][y])
    num = size // 2
    return "(" + quadtree(x, y, num) + quadtree(x, y + num, num) + quadtree(x + num, y, num) + quadtree(x + num, y + num, num) + ")"


print(quadtree(0, 0, N))