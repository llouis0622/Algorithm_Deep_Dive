import sys

input = sys.stdin.readline
arr = [int(input()) for _ in range(9)]
tot = sum(arr)
num = tot - 100
for i in range(9):
    for j in range(i + 1, 9):
        if arr[i] + arr[j] == num:
            res = [arr[x] for x in range(9) if x != i and x != j]
            res.sort()
            for k in res:
                print(k)
            exit()
