import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
A = [[] for _ in range(N + 1)]
reverseA = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for i in range(M):
    S, E, V = map(int, input().split())
    A[S].append((E, V))
    reverseA[E].append((S, V))
    indegree[E] += 1

startDosi, endDosi = map(int, input().split())

queue = deque()
queue.append(startDosi)
result = [0] * (N + 1)

while queue:
    now = queue.popleft()

    for next in A[now]:
        indegree[next[0]] -= 1
        result[next[0]] = max(result[next[0]], result[now] + next[1])

        if indegree[next[0]] == 0:
            queue.append(next[0])

resultCount = 0
visited = [False] * (N + 1)
queue.clear()
queue.append(endDosi)
visited[endDosi] = True

while queue:
    now = queue.popleft()

    for next in reverseA[now]:
        if result[next[0]] + next[1] == result[now]:
            resultCount += 1

            if not visited[next[0]]:
                visited[next[0]] = True
                queue.append(next[0])

print(result[endDosi])
print(resultCount)