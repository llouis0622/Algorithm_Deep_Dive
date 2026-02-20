T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = M % N
    print(f"#{i} {arr[idx]}")