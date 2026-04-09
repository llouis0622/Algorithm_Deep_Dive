def solution(citations):
    citations.sort(reverse=True)
    for i, j in enumerate(citations):
        if j < i + 1:
            return i
    return len(citations)
