T = int(input())

for i in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    A = [0] * (V + 1)
    B = [0] * (V + 1)
    for j in range(0, 2 * E, 2):
        x = arr[j]
        s = arr[j + 1]
        if A[x] == 0:
            A[x] = s
        else:
            B[x] = s
    cnt = 0
    stack = [N]
    while stack:
        x = stack.pop()
        cnt += 1
        if A[x]:
            stack.append(A[x])
        if B[x]:
            stack.append(B[x])
    print(f"#{i} {cnt}")