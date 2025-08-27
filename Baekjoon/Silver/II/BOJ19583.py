import sys

input = sys.stdin.readline
S, E, Q = input().split()
s = int(S[:2]) * 60 + int(S[3:])
e = int(E[:2]) * 60 + int(E[3:])
q = int(Q[:2]) * 60 + int(Q[3:])
num = set()
res = set()
ans = 0
while True:
    temp = input()
    if not temp:
        break
    temp = temp.strip()
    if not temp:
        continue
    t, n = temp.split()
    m = int(t[:2]) * 60 + int(t[3:])
    if m <= s:
        num.add(n)
    elif e <= m <= q:
        if n in num and n not in res:
            res.add(n)
            ans += 1
print(ans)