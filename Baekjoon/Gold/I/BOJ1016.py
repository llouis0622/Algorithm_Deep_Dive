import math

N, M = map(int, input().split())
bl = [False] * (M - N + 1)

for i in range(2, int(math.sqrt(M) + 1)):
    num = i * i
    s = int(N / num)

    if N % num != 0:
        s += 1

    for j in range(s, int(M / num) + 1):
        bl[int((j * num) - N)] = True

cnt = 0

for i in range(0, M - N + 1):
    if not bl[i]:
        cnt += 1

print(cnt)