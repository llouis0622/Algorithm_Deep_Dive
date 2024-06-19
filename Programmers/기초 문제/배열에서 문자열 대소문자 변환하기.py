def solution(strArr):
    return [j.lower() if i % 2 == 0 else j.upper() for i, j in enumerate(strArr)]