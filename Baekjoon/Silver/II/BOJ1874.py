N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

stk = []
num = 1
res = True
ans = []

for i in range(N):
    idx = A[i]

    if idx >= num:
        while idx >= num:
            stk.append(num)
            num += 1
            ans.append('+')

        stk.pop()
        ans.append('-')
    else:
        n = stk.pop()

        if n > idx:
            print("NO")
            res = False
            break
        else:
            ans.append('-')

if res:
    for i in ans:
        print(i)