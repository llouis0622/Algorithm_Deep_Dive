def solution(n, lost, reserve):
    arr = set(reserve) - set(lost)
    lst = set(lost) - set(reserve)
    for i in sorted(arr):
        if i - 1 in lst:
            lst.remove(i - 1)
        elif i + 1 in lst:
            lst.remove(i + 1)
    return n - len(lst)