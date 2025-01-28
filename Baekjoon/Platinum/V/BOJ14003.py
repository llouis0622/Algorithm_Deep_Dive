import bisect


def sequence(n, arr):
    lst = []
    indices = [0] * n
    for i, num in enumerate(arr):
        pos = bisect.bisect_left(lst, num)
        if pos == len(lst):
            lst.append(num)
        else:
            lst[pos] = num
        indices[i] = pos
    num = len(lst)
    res = []
    temp = num - 1
    for i in range(n - 1, -1, -1):
        if indices[i] == temp:
            res.append(arr[i])
            temp -= 1
    return num, res[::-1]


n = int(input())
arr = list(map(int, input().split()))
length, sequence = sequence(n, arr)
print(length)
print(*sequence)