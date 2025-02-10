def backtrack(row, n, cols, diag1, diag2, count):
    if row == n:
        return count + 1
    for col in range(n):
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue
        count = backtrack(row + 1, n, cols | {col}, diag1 | {row - col}, diag2 | {row + col}, count)
    return count

def solution(n):
    return backtrack(0, n, set(), set(), set(), 0)