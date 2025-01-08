import sys
input = sys.stdin.readline

F = [0] * 21
S = [0] * 21
visited = [False] * 21
N = int(input())
F[0] = 1
for i in range(1, N + 1):
    F[i] = F[i - 1] * i
lst = list(map(int, input().split()))
if lst[0] == 1:
    K = lst[1]
    for i in range(1, N + 1):
        cnt = 1
        for j in range(1, N + 1):
            if visited[j]:
                continue
            if K <= cnt * F[N - i]:
                K -= (cnt - 1) * F[N - i]
                S[i] = j
                visited[j] = True
                break
            cnt += 1
    for i in range(1, N + 1):
        print(S[i], end=' ')
else:
    K = 1
    for i in range(1, N + 1):
        cnt = 0
        for j in range(1, lst[i]):
            if not visited[j]:
                cnt += 1
        K += cnt * F[N - i]
        visited[lst[i]] = True
    print(K)