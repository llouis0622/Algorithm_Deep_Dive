def solution(N, number):
    DP = [set() for _ in range(9)]
    for i in range(1, 9):
        DP[i].add(int(str(N) * i))
        for j in range(1, i):
            for k in DP[j]:
                for l in DP[i - j]:
                    DP[i].add(k + l)
                    DP[i].add(k - l)
                    DP[i].add(k * l)
                    if l != 0:
                        DP[i].add(k // l)
        if number in DP[i]:
            return i
    return -1