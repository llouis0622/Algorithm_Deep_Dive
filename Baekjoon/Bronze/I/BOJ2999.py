import sys

s = sys.stdin.readline().strip()
n = len(s)
R = 1
for i in range(1, n + 1):
    if n % i == 0 and i <= n // i:
        R = i
C = n // R
temp = [s[i * R:(i + 1) * R] for i in range(C)]
ans = []
for r in range(R):
    for c in range(C):
        ans.append(temp[c][r])
print(''.join(ans))