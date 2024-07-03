def solution(polynomial):
    pol = polynomial.split(' + ')
    x = 0
    num = 0
    for i in pol:
        if 'x' in i:
            if i == 'x':
                x += 1
            else:
                x += int(i.replace('x', ''))
        else:
            num += int(i)
    ans = []
    if x > 0:
        ans.append(f"{x}x" if x > 1 else "x")
    if num > 0:
        ans.append(str(num))
    return ' + '.join(ans)