import sys

readline = sys.stdin.readline
n, m = map(int, readline().split())
num = {}
res = {}
for _ in range(n):
    s = readline().strip()
    cnt = int(readline().strip())
    temp = [readline().strip() for _ in range(cnt)]
    temp.sort()
    num[s] = temp
    for i in temp:
        res[i] = s
ans = []
for _ in range(m):
    key = readline().strip()
    t = int(readline().strip())
    if t == 0:
        ans.extend(num[key])
    else:
        ans.append(res[key])
print("\n".join(ans))