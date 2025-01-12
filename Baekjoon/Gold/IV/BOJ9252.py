import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

A = list(input())
A.pop()
B = list(input())
B.pop()
DP = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
Path = []
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
print(DP[len(A)][len(B)])


def getText(r, c):
    if r == 0 or c == 0:
        return
    if A[r - 1] == B[c - 1]:
        Path.append(A[r - 1])
        getText(r - 1, c - 1)
    else:
        if DP[r - 1][c] > DP[r][c - 1]:
            getText(r - 1, c)
        else:
            getText(r, c - 1)


getText(len(A), len(B))
for i in range(len(Path) - 1, -1, -1):
    print(Path.pop(i), end='')
print()