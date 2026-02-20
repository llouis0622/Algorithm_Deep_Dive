T = int(input().strip())
for i in range(1, T + 1):
    A = input().strip()
    B = input().strip()
    N = len(A)
    M = len(B)
    ans = 0
    for j in range(M - N + 1):
        if B[j:j + N] == A:
            ans = 1
            break
    print(f"#{i} {ans}")