def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    ans = 0
    for i in range(row_begin - 1, row_end):
        num = i + 1
        s = sum(v % num for v in data[i])
        ans ^= s
    return ans