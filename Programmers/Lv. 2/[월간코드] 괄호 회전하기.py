def solution(s):
    n = len(s)
    ans = 0
    for x in range(n):
        t = s[x:] + s[:x]
        stack = []
        check = True
        for ch in t:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack:
                    check = False
                    break
                top = stack.pop()
                if not ((top == '(' and ch == ')') or
                        (top == '[' and ch == ']') or
                        (top == '{' and ch == '}')):
                    check = False
                    break
        if check and not stack:
            ans += 1
    return ans