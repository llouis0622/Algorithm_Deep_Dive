import sys

sys.setrecursionlimit(10 ** 7)
N = list(map(int, sys.stdin.buffer.read().split()))
n = len(N)
idx = 0
temp = []


def DFS(bound):
    global idx
    if idx >= n or N[idx] > bound:
        return
    root = N[idx]
    idx += 1
    DFS(root)
    DFS(bound)
    temp.append(root)


DFS(10 ** 9)
sys.stdout.write("\n".join(map(str, temp)))