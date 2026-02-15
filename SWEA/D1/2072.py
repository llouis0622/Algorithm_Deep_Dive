T = int(input())
for i in range(1, T + 1):
    N = list(map(int, input().split()))
    A = sum(n for n in N if n % 2 == 1)
    print(f"#{i} {A}")