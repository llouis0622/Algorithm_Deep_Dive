def solution(elements):
    n = len(elements)
    elements += elements
    temp = set()
    for l in range(1, n + 1):
        res = sum(elements[:l])
        temp.add(res)
        for i in range(1, n):
            res = res - elements[i - 1] + elements[i + l - 1]
            temp.add(res)
    return len(temp)