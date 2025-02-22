n = int(input())
d = [0] * (n + 1)
pre = [0] * (n + 1)
for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    pre[i] = i - 1
    if i % 2 == 0 and d[i] > d[i // 2] + 1:
        d[i] = d[i // 2] + 1
        pre[i] = i // 2
    if i % 3 == 0 and d[i] > d[i // 3] + 1:
        d[i] = d[i // 3] + 1
        pre[i] = i // 3
print(d[n])
cur = n
while True:
    print(cur, end=' ')
    if cur == 1:
        break
    cur = pre[cur]