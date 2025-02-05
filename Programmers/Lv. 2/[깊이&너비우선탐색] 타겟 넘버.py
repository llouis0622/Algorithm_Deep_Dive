def solution(numbers, target):
    cnt = 0
    stack = [(0, 0)]
    while stack:
        idx, sum = stack.pop()
        if idx == len(numbers):
            if sum == target:
                cnt += 1
        else:
            stack.append((idx + 1, sum + numbers[idx]))
            stack.append((idx + 1, sum - numbers[idx]))
    return cnt