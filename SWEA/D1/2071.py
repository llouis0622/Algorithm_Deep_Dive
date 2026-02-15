T = int(input())
for i in range(1, T + 1):
    N = list(map(int, input().split()))
    A = round(sum(N) / 10)
    print(f"#{i} {A}")