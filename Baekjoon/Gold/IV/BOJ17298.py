import sys

n = int(input())
ans = [0] * n
lst = list(map(int, input().split()))
stk = []

for i in range(n):
    while stk and lst[stk[-1]] < lst[i]:
        ans[stk.pop()] = lst[i]
    stk.append(i)

while stk:
    ans[stk.pop()] = -1

for i in range(n):
    sys.stdout.write(str(ans[i]) + " ")