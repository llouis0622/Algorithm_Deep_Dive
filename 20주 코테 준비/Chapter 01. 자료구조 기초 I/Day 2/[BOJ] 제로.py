import sys

input = sys.stdin.readline
K = int(input())
stack = []
for _ in range(K):
    N = int(input())
    if N == 0:
        stack.pop()
    else:
        stack.append(N)
print(sum(stack))
