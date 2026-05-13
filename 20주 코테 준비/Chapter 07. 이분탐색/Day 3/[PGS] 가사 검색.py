from bisect import bisect_left, bisect_right


def cnt(arr, left, right):
    return bisect_right(arr, right) - bisect_left(arr, left)


def solution(words, queries):
    arr = [[] for _ in range(10001)]
    temp = [[] for _ in range(10001)]
    for i in words:
        arr[len(i)].append(i)
        temp[len(i)].append(i[::-1])
    for i in range(10001):
        arr[i].sort()
        temp[i].sort()
    ans = []
    for i in queries:
        length = len(i)
        if i[0] != '?':
            left = i.replace('?', 'a')
            right = i.replace('?', 'z')
            ans.append(cnt(arr[length], left, right))
        else:
            i = i[::-1]
            left = i.replace('?', 'a')
            right = i.replace('?', 'z')
            ans.append(cnt(temp[length], left, right))
    return ans
