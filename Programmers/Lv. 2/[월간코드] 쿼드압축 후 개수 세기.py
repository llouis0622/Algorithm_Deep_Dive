def solution(arr):
    stack = [(0, 0, len(arr))]
    res = [0, 0]
    while stack:
        x, y, size = stack.pop()
        num = arr[x][y]
        check = True
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != num:
                    check = False
                    break
            if not check:
                break
        if check:
            res[num] += 1
        else:
            temp = size // 2
            stack.append((x, y, temp))
            stack.append((x, y + temp, temp))
            stack.append((x + temp, y, temp))
            stack.append((x + temp, y + temp, temp))
    return res