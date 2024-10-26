import sys

input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()), i))
    
num = 0
lst = sorted(A)

for i in range(N):
    if num < lst[i][1] - i:
        num = lst[i][1] - i
print(num + 1)