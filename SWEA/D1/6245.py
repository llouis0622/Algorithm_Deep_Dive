N = 0
while True:
    try:
        S = input().split()
        if not S:
            break
        t, m = S
        m = int(m)
        if t == 'D':
            N += m
        elif t == 'W':
            N -= m
    except:
        break
print(f"잔액: {N}")