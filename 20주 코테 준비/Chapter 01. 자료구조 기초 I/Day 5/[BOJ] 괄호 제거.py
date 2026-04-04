import sys

input = sys.stdin.readline
arr = input().strip()
stack = []
pairs = []
for i, j in enumerate(arr):
    if j == '(':
        stack.append(i)
    elif j == ')':
        pairs.append((stack.pop(), i))
res = set()
num = len(pairs)
for i in range(1, 1 << num):
    temp =  set()
    for j in range(num):
        if i & (1 << j):
            temp.add(pairs[j][0])
            temp.add(pairs[j][1])
    ele = ''.join(y for x, y in enumerate(arr) if x not in temp)
    res.add(ele)
print('\n'.join(sorted(res)))
