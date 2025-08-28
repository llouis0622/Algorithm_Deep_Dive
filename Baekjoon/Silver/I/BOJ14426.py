import sys

n, m = map(int, sys.stdin.readline().split())
trie = {}
for _ in range(n):
    s = sys.stdin.readline().strip()
    temp = trie
    for i in s:
        if i not in temp:
            temp[i] = {}
        temp = temp[i]
ans = 0
for _ in range(m):
    q = sys.stdin.readline().strip()
    temp = trie
    check = True
    for i in q:
        if i in temp:
            temp = temp[i]
        else:
            check = False
            break
    if check:
        ans += 1
print(ans)