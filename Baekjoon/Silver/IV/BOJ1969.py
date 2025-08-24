import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dna = [input().strip() for _ in range(n)]
temp = ['A', 'C', 'G', 'T']
ans = []
res = 0
for j in range(m):
    cnt = [0, 0, 0, 0]
    for i in range(n):
        x = dna[i][j]
        if x == 'A':
            cnt[0] += 1
        elif x == 'C':
            cnt[1] += 1
        elif x == 'G':
            cnt[2] += 1
        else:
            cnt[3] += 1
    num = max(cnt)
    for k in range(4):
        if cnt[k] == num:
            ans.append(temp[k])
            break
    res += n - num
print(''.join(ans))
print(res)