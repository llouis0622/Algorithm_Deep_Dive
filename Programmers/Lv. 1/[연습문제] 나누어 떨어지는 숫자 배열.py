def solution(arr, divisor):
    result = [i for i in arr if i % divisor == 0]
    if not result:
        return [-1]
    return sorted(result)