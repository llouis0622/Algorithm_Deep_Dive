T = int(input())
for i in range(1, T + 1):
    N, S = map(str, input().split())
    A = ''.join(format(int(j, 16), '04b') for j in S)
    print(f'#{i} {A}')