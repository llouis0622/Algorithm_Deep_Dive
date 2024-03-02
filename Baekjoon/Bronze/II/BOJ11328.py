N = int(input())
for _ in range(N):
    A, B = map(sorted, list(input().split()))
    print('Possible' if A == B else 'Impossible')