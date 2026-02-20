T = int(input().strip())
for i in range(1, T + 1):
    N = int(input().strip()) // 10
    A = [0] * (N + 2)
    A[1] = 1
    A[2] = 3
    for j in range(3, N + 1):
        A[j] = A[j - 1] + 2 * A[j - 2]
    print(f"#{i} {A[N]}")