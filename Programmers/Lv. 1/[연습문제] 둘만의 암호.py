def solution(s, skip, index):
    arr = [chr(i) for i in range(97, 123)]
    lst = [i for i in arr if i not in skip]
    res = []
    for i in s:
        idx = lst.index(i)
        temp = (idx + index) % len(lst)
        res.append(lst[temp])
    return ''.join(res)