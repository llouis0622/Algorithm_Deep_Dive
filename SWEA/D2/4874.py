T = int(input().strip())
ops = {"+", "-", "*", "/"}
for i in range(1, T + 1):
    N = input().split()
    A = []
    check = True
    if not N or N[-1] != '.':
        check = False
    else:
        for j in N:
            if j == '.':
                if len(A) != 1:
                    check = False
                break
            if j in ops:
                if len(A) < 2:
                    check = False
                    break
                b = A.pop()
                a = A.pop()
                if j == '+':
                    A.append(a + b)
                elif j == '-':
                    A.append(a - b)
                elif j == '*':
                    A.append(a * b)
                else:
                    if b == 0:
                        check = False
                        break
                    A.append(a // b)
            else:
                try:
                    A.append(int(j))
                except:
                    check = False
                    break
    print(f"#{i} {A[0] if check else 'error'}")