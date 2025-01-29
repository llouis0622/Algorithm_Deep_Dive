MOD = 1000000007
N = int(input())
if N % 2 == 1:
    print(0)
else:
    N //= 2
    base_matrix = [
        [4, -1, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]
    ]
    initial_vector = [3, 1, 0, 0]
    result_matrix = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
    base = base_matrix
    power = N - 1
    while power:
        if power % 2 == 1:
            result_matrix = [[sum(x * y % MOD for x, y in zip(row, col)) % MOD for col in zip(*base)] for row in result_matrix]
        base = [[sum(x * y % MOD for x, y in zip(row, col)) % MOD for col in zip(*base)] for row in base]
        power //= 2
    result = sum(result_matrix[0][i] * initial_vector[i] for i in range(4)) % MOD
    print(result)