T = int(input())


def win(a, b, card):
    x = card[a]
    y = card[b]
    if x == y:
        return a
    if (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
        return a
    return b


def game(l, r, card):
    if l == r:
        return l
    m = (l + r) // 2
    left = game(l, m, card)
    right = game(m + 1, r, card)
    return win(left, right, card)


for i in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    card = [0] + arr
    ans = game(1, N, card)
    print(f"#{i} {ans}")