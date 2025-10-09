import sys

s = sys.stdin.readline().rstrip()
n = sys.stdin.readline().rstrip()
stack = []
num = len(n)
res = n[-1]
temp = list(n)
for i in s:
    stack.append(i)
    if i == res and len(stack) >= num:
        if stack[-num:] == temp:
            del stack[-num:]
ans = ''.join(stack)
print(ans if ans else "FRULA")