def solution(numbers, k):
    idx = (2 * (k - 1)) % len(numbers)
    return numbers[idx]