import sys

input = sys.stdin.read
data = input().splitlines()

N, S = map(int, data[0].split())
arr = list(map(int, data[1].split()))
cnt = 0


def BFS(idx, total):
    global cnt
    if idx >= N:
        return
    total += arr[idx]
    if total == S:
        cnt += 1
    BFS(idx + 1, total)
    BFS(idx + 1, total - arr[idx])


BFS(0, 0)
print(cnt)