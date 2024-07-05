def solution(num, total):
    ans = (total - (num * (num - 1)) // 2) // num
    return [ans + i for i in range(num)]