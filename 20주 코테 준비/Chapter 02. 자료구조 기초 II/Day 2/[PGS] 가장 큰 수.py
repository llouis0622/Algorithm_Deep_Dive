def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    ans = ''.join(numbers)
    return '0' if ans[0] == '0' else ans
