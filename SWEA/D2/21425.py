T = int(input())
for _ in range(T):
    A, B, N = map(int, input().split())
    if A > B:
        A, B = B, A
    cnt = 0
    while B <= N:
        A, B = B, A + B
        cnt += 1
    print(cnt)