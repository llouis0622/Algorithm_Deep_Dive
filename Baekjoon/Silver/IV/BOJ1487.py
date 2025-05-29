N = int(input())
temp = [tuple(map(int, input().split())) for _ in range(N)]
num = 0
ans = 0
for i in set(x for x, _ in temp):
    p = 0
    for price, res in temp:
        if price >= i:
            margin = i - res
            if margin > 0:
                p += margin
    if p > num or (p == num and i < ans):
        num = p
        ans = i
print(ans if num > 0 else 0)