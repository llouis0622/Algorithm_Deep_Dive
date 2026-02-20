T = int(input().strip())
for i in range(1, T + 1):
    A = input().strip()
    B = input().strip()
    D = {}
    for j in B:
        D[j] = D.get(j, 0) + 1
    ans = 0
    for j in A:
        if j in D and D[j] > ans:
            ans = D[j]
    print(f"#{i} {ans}")