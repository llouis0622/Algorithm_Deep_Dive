def solution(s):
    arr = []
    for i in s:
        if i == '(':
            arr.append('(')
        else:
            if arr:
                arr.pop()
            else:
                return False
    return not arr
