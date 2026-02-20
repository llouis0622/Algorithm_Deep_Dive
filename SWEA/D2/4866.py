T = int(input().strip())
for i in range(1, T + 1):
    S = input().strip()
    A = []
    check = 1
    for j in S:
        if j == '(' or j == '{':
            A.append(j)
        elif j == ')':
            if not A or A[-1] != '(':
                check = 0
                break
            A.pop()
        elif j == '}':
            if not A or A[-1] != '{':
                check = 0
                break
            A.pop()
    if A:
        check = 0
    print(f"#{i} {check}")