def backtrack(cur, n, check1, check2, check3, cnt):
    if cur == n:
        cnt[0] += 1
        return
    for i in range(n):
        if check1[i] or check2[i + cur] or check3[cur - i + n - 1]:
            continue
        check1[i] = True
        check2[i + cur] = True
        check3[cur - i + n - 1] = True
        backtrack(cur + 1, n, check1, check2, check3, cnt)
        check1[i] = False
        check2[i + cur] = False
        check3[cur - i + n - 1] = False


def nqueen(n):
    check1 = [False] * 40
    check2 = [False] * 40
    check3 = [False] * 40
    cnt = [0]
    backtrack(0, n, check1, check2, check3, cnt)
    return cnt[0]


n = int(input())
print(nqueen(n))