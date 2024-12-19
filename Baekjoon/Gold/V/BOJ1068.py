import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
visited = [False] * (N)
tree = [[] for _ in range(N)]
answer = 0
p = list(map(int, input().split()))

for i in range(N):
    if p[i] != -1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i


def DFS(number):
    global answer
    visited[number] = True
    cNode = 0

    for i in tree[number]:
        if not visited[i] and i != deleteNode:
            cNode += 1
            DFS(i)

    if cNode == 0:
        answer += 1


deleteNode = int(input())

if deleteNode == root:
    print(0)
else:
    DFS(root)
    print(answer)