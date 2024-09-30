def solution(mats, park):
    mats.sort(reverse=True)
    rows = len(park)
    cols = len(park[0])

    def put(mat, row, col):
        if row + mat > rows or col + mat > cols:
            return False
        for i in range(row, row + mat):
            for j in range(col, col + mat):
                if park[i][j] != "-1":
                    return False
        return True

    for k in mats:
        for i in range(rows):
            for j in range(cols):
                if put(k, i, j):
                    return k
    return -1