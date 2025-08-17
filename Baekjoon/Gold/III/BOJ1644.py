def prime(num):
    check = [True] * (num + 1)
    check[0] = check[1] = False
    for i in range(2, int(num ** 0.5) + 1):
        if check[i]:
            for j in range(i * i, num + 1, i):
                check[j] = False
    return [i for i, j in enumerate(check) if j]


n = int(input())
temp = prime(n)
cnt = 0
l = r = 0
tot = 0
while True:
    if tot >= n:
        if tot == n:
            cnt += 1
        tot -= temp[l]
        l += 1
    elif r == len(temp):
        break
    else:
        tot += temp[r]
        r += 1
print(cnt)