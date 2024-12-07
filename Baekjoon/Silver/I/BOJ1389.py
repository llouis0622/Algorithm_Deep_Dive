import sys

N, M = map(int, input().split())
distance = [[sys.maxsize for j in range(N + 1)] for i in range(N + 1)]

for i in range(1, N + 1):
    distance[i][i] = 0

for i in range(M):
    s, e = map(int, input().split())
    distance[s][e] = 1
    distance[e][s] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

Min = sys.maxsize
Answer = -1

for i in range(1, N + 1):
    temp = 0

    for j in range(1, N + 1):
        temp += distance[i][j]

    if Min > temp:
        Min = temp
        Answer = i

print(Answer)