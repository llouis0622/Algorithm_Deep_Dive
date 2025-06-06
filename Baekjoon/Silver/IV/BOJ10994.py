def star(n, x, y):
    if n == 0:
        return
    num = 4 * n - 3
    for i in range(num):
        arr[x][y + i] = '*'
        arr[x + num - 1][y + i] = '*'
        arr[x + i][y] = '*'
        arr[x + i][y + num - 1] = '*'
    star(n - 1, x + 2, y + 2)


n = int(input())
temp = 4 * n - 3
arr = [[' ' for _ in range(temp)] for _ in range(temp)]
star(n, 0, 0)
for i in arr:
    print(''.join(i))