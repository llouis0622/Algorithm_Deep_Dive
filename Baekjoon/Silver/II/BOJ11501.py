T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    temp = ans = 0
    for price in reversed(prices):
        if price > temp:
            temp = price
        else:
            ans += temp - price
    print(ans)