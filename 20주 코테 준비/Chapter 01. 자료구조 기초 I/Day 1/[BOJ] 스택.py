import sys

input = sys.stdin.readline
N = int(input())
stack = []

for _ in range(N):
    op = input().split()

    if op[0] == 'push':
        stack.append(int(op[1]))
    elif op[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif op[0] == 'size':
        print(len(stack))
    elif op[0] == 'empty':
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)
