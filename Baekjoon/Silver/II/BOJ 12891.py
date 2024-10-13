arr = [0] * 4
lst = [0] * 4
chk = 0


def myadd(c):
    global arr, lst, chk

    if c == 'A':
        lst[0] += 1
        if lst[0] == arr[0]:
            chk += 1
    elif c == 'C':
        lst[1] += 1
        if lst[1] == arr[1]:
            chk += 1
    elif c == 'G':
        lst[2] += 1
        if lst[2] == arr[2]:
            chk += 1
    elif c == 'T':
        lst[3] += 1
        if lst[3] == arr[3]:
            chk += 1


def myremove(c):
    global arr, lst, chk

    if c == 'A':
        if lst[0] == arr[0]:
            chk -= 1
        lst[0] -= 1
    elif c == 'C':
        if lst[1] == arr[1]:
            chk -= 1
        lst[1] -= 1
    elif c == 'G':
        if lst[2] == arr[2]:
            chk -= 1
        lst[2] -= 1
    elif c == 'T':
        if lst[3] == arr[3]:
            chk -= 1
        lst[3] -= 1


S, P = map(int, input().split())
Result = 0
A = list(input())
arr = list(map(int, input().split()))

for i in range(4):
    if arr[i] == 0:
        chk += 1

for i in range(P):
    myadd(A[i])

if chk == 4:
    Result += 1

for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])

    if chk == 4:
        Result += 1

print(Result)