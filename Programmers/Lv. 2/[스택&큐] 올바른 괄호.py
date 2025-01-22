def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
    return not stack