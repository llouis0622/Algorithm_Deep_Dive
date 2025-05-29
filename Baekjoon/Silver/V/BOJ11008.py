T = int(input())
for _ in range(T):
    s, p = input().split()
    i = 0
    ans = 0
    while i < len(s):
        if s[i:i + len(p)] == p:
            ans += 1
            i += len(p)
        else:
            ans += 1
            i += 1
    print(ans)