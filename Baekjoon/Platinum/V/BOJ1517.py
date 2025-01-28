import sys

input = sys.stdin.readline
res = 0


def merge_sort(s, e):
    global res

    if e - s < 1:
        return

    m = int(s + (e - s) / 2)
    merge_sort(s, m)
    merge_sort(m + 1, e)

    for i in range(s, e + 1):
        lst[i] = A[i]

    k = s
    idx1 = s
    idx2 = m + 1

    while idx1 <= m and idx2 <= e:
        if lst[idx1] > lst[idx2]:
            A[k] = lst[idx2]
            res = res + idx2 - k
            k += 1
            idx2 += 1
        else:
            A[k] = lst[idx1]
            k += 1
            idx1 += 1

    while idx1 <= m:
        A[k] = lst[idx1]
        k += 1
        idx1 += 1

    while idx2 <= e:
        A[k] = lst[idx2]
        k += 1
        idx2 += 1


N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)

lst = [0] * int(N + 1)
merge_sort(1, N)

print(res)