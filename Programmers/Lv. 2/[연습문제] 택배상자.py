def solution(order):
    stack = []
    i = 1
    ans = 0
    for o in order:
        while i <= o:
            stack.append(i)
            i += 1
        if stack[-1] == o:
            stack.pop()
            ans += 1
        else:
            break
    return ans