import sys

input = sys.stdin.read
data = input().splitlines()
N = int(data[0])
logs = data[1:N + 1]
K = int(data[N + 1])
lst = set(data[N + 2:N + 2 + K])
check = {}
for i, name in enumerate(logs):
    check[name] = i
temp = []
num = []
for name, time in check.items():
    if name in lst:
        temp.append((time, name))
    else:
        num.append((time, name))
temp.sort(reverse=True)
num.sort(reverse=True)
for _, name in temp + num:
    print(name)