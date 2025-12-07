import sys

n = int(sys.stdin.readline())
temp = []
for i in range(n):
    x, h = map(int, sys.stdin.readline().split())
    l = x - h
    r = x + h
    temp.append((l, 0, i))
    temp.append((r, 1, i))
temp.sort()
for i in range(1, len(temp)):
    if temp[i][0] == temp[i - 1][0]:
        print("NO")
        sys.exit(0)
stack = []
for p, t, i in temp:
    if t == 0:
        stack.append(i)
    else:
        if not stack or stack[-1] != i:
            print("NO")
            sys.exit(0)
        stack.pop()
print("YES")