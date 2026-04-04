import sys

input = sys.stdin.readline
arr = input().strip()
stack = []
res = []
check = False
for i in arr:
    if i == '<':
        while stack:
            res.append(stack.pop())
        check = True
        res.append(i)
    elif i == '>':
        check = False
        res.append(i)
    elif check:
        res.append(i)
    elif i == ' ':
        while stack:
            res.append(stack.pop())
        res.append(' ')
    else:
        stack.append(i)
while stack:
    res.append(stack.pop())
print(''.join(res))
