import sys

readline = sys.stdin.readline
K, L = map(int, readline().split())
temp = {}
for _ in range(L):
    s = readline().strip()
    if s in temp:
        del temp[s]
    temp[s] = True
cnt = 0
ans = []
for k in temp.keys():
    ans.append(k)
    cnt += 1
    if cnt == K:
        break
print("\n".join(ans))