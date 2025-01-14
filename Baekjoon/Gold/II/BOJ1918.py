def postfix(temp):
    lst = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stk = []
    res = []
    for i in temp:
        if i.isalpha():
            res.append(i)
        elif i == '(':
            stk.append(i)
        elif i == ')':
            while stk and stk[-1] != '(':
                res.append(stk.pop())
            stk.pop()
        else:
            while stk and lst[stk[-1]] >= lst[i]:
                res.append(stk.pop())
            stk.append(i)
    while stk:
        res.append(stk.pop())
    return ''.join(res)


temp = input().strip()
print(postfix(temp))