import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num2name = ['']
name2num = {}
for i in range(1, n + 1):
    name = input().strip()
    num2name.append(name)
    name2num[name] = i
for _ in range(m):
    q = input().strip()
    if q.isdigit():
        print(num2name[int(q)])
    else:
        print(name2num[q])