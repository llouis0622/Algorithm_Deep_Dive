import sys

input = sys.stdin.readline
A = input().strip()
stack = []
ans = 0
for i in range(len(A)):
    if A[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if A[i - 1] == '(':
            ans += len(stack)
        else:
            ans += 1
print(ans)
