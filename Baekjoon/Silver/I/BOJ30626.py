import sys

data = sys.stdin
n = int(data.readline())
temp = [0] * 361
for _ in range(n):
    line = data.readline().split()
    a = int(line[0])
    b = int(line[1])
    if b < 180:
        s = (a + 180 - b) % 360
        e = (a + 180 + b) % 360
        if s <= e:
            temp[s] += 1
            temp[e + 1] -= 1
        else:
            temp[s] += 1
            temp[360] -= 1
            temp[0] += 1
            temp[e + 1] -= 1
    else:
        L = (a + 91) % 360
        R = (a + 269) % 360
        if L <= R:
            temp[L] += 1
            temp[R + 1] -= 1
        else:
            temp[L] += 1
            temp[360] -= 1
            temp[0] += 1
            temp[R + 1] -= 1
        temp[a] += 1
        if a < 359:
            temp[a + 1] -= 1
        else:
            temp[360] -= 1
cnt = 0
num = 0
for i in range(360):
    num += temp[i]
    if num > 0:
        cnt += 1
print(cnt)