T = int(input().strip())
for i in range(1, T + 1):
    S = input().strip()
    A = []
    for j in S:
        if A and A[-1] == j:
            A.pop()
        else:
            A.append(j)
    print(f"#{i} {len(A)}")