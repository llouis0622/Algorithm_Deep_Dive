import sys

input = sys.stdin.readline

n = int(input())
U = [int(input()) for _ in range(n)]
U.sort()
num = set()
for i in range(n):
    for j in range(n):
        num.add(U[i] + U[j])
for k in range(n - 1, -1, -1):
    for l in range(n):
        if (U[k] - U[l]) in num:
            print(U[k])
            exit()