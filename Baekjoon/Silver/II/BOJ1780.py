import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
paper = [list(map(int, line.split())) for line in data[1:N + 1]]
cnt = {-1: 0, 0: 0, 1: 0}


def check(x, y, size):
    temp = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != temp:
                return False
    return True


def divide(x, y, size):
    if check(x, y, size):
        cnt[paper[x][y]] += 1
        return
    num = size // 3
    for i in range(3):
        for j in range(3):
            divide(x + i * num, y + j * num, num)


divide(0, 0, N)
print(cnt[-1])
print(cnt[0])
print(cnt[1])