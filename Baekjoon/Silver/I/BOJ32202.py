MOD = 10 ** 9 + 7


def solve(N):
    a, b = 1, 2
    for _ in range(2, N + 1):
        num_a = b
        num_b = (a + b) * 2 % MOD
        a, b = num_a, num_b
    return (a + b) % MOD


N = int(input())
print(solve(N))