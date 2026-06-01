def solution(number, k):
    stack = []
    for i in number:
        while k > 0 and stack and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)
    return ''.join(stack[:-k] if k else stack)
