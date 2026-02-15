T = int(input())
for i in range(1, T + 1):
    A, B = map(int, input().split())
    if A > B:
        N = ">"
    elif A < B:
        N = "<"
    else:
        N = "="
    print(f"#{i} {N}")