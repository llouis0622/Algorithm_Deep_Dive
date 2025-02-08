def check(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack


def split(s):
    cnt = 0
    for i, c in enumerate(s):
        cnt += 1 if c == '(' else -1
        if cnt == 0:
            return s[:i + 1], s[i + 1:]


def bracket(s):
    return ''.join('(' if c == ')' else ')' for c in s)


def solution(p):
    if not p:
        return p
    u, v = split(p)
    if check(u):
        return u + solution(v)
    return '(' + solution(v) + ')' + bracket(u[1:-1])