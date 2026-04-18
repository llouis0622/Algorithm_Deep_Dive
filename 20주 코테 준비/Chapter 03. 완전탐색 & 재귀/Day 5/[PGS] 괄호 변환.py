def split_uv(s):
    left, right = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return s[:i + 1], s[i + 1:]


def is_correct(s):
    balance = 0
    for i in s:
        if i == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return True


def reverse_bracket(s):
    return ''.join(')' if i == '(' else '(' for i in s)


def solution(p):
    if not p:
        return ''
    u, v = split_uv(p)
    return u + solution(v) if is_correct(u) else '(' + solution(v) + ')' + reverse_bracket(u[1:-1])
