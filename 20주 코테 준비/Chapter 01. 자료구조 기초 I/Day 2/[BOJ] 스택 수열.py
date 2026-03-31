import sys

input = sys.stdin.readline
N = int(input())
A = [int(input()) for _ in range(N)]
stack = []
result = []
cur = 0
for i in A:
    if i > cur:
        while cur < i:
            cur += 1
            stack.append(cur)
            result.append('+')
        stack.pop()
        result.append('-')
    else:
        if stack and stack[-1] == i:
            stack.pop()
            result.append('-')
        else:
            print('NO')
            break
else:
    print('\n'.join(result))
