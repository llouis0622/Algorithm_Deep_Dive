def solution(dirs):
    x, y = 0, 0
    check = set()
    coor = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    for d in dirs:
        dx, dy = coor[d]
        nx, ny = x + dx, y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            num = ((x, y), (nx, ny))
            temp = ((nx, ny), (x, y))
            check.add(num)
            check.add(temp)
            x, y = nx, ny
    return len(check) // 2