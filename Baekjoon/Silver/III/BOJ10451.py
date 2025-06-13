T = int(input())
for _ in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    check = [False] * (N + 1)
    cnt = 0
    for i in range(1, N + 1):
        if not check[i]:
            num = i
            while not check[num]:
                check[num] = True
                num = temp[num - 1]
            cnt += 1
    print(cnt)