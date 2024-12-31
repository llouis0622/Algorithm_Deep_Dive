def key(temp):
    res = []
    for i in temp:
        l_stk = []
        r_stk = []
        for j in i:
            if j == '<':
                if l_stk:
                    r_stk.append(l_stk.pop())
            elif j == '>':
                if r_stk:
                    l_stk.append(r_stk.pop())
            elif j == '-':
                if l_stk:
                    l_stk.pop()
            else:
                l_stk.append(j)
        res.append(''.join(l_stk + r_stk[::-1]))
    return res


T = int(input())
temp = [input().strip() for _ in range(T)]
res = key(temp)
print("\n".join(res))