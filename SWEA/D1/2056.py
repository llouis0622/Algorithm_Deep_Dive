T = int(input())
A = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
for i in range(1, T + 1):
    S = input().strip()
    Y = S[:4]
    M = int(S[4:6])
    D = int(S[6:8])
    if 1 <= M <= 12 and 1 <= D <= A[M]:
        print(f"#{i} {Y}/{M:02d}/{D:02d}")
    else:
        print(f"#{i} -1")