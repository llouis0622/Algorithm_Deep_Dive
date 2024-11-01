ans = 0
A = list(map(str, input().split("-")))


def func_sum(i):
    sum = 0
    temp = str(i).split("+")

    for i in temp:
        sum += int(i)

    return sum


for i in range(len(A)):
    temp = func_sum(A[i])

    if i == 0:
        ans += temp
    else:
        ans -= temp

print(ans)