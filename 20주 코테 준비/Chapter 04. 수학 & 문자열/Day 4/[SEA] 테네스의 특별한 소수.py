T = int(input())
MAX = 10 ** 6
prime = [True] * (MAX + 1)
prime[0] = prime[1] = False
for i in range(2, int(MAX ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, MAX + 1, i):
            prime[j] = False
for i in range(1, T + 1):
    D, A, B = map(int, input().split())
    D = str(D)
    cnt = 0
    for j in range(A, B + 1):
        if prime[j] and D in str(j):
            cnt += 1
    print(f'#{i} {cnt}')
