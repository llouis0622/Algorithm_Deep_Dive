import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
num = []
temp = None
for i in lst:
    if i != temp:
        num.append(i)
        temp = i
res = []


def DFS(start, depth):
    if depth == M:
        print(' '.join(map(str, res)))
        return
    for i in range(start, len(num)):
        res.append(num[i])
        DFS(i, depth + 1)
        res.pop()


DFS(0, 0)