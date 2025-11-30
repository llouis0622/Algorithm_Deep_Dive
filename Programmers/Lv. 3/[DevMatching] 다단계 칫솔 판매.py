def solution(enroll, referral, seller, amount):
    n = len(enroll)
    idx = {name: i for i, name in enumerate(enroll)}
    temp = [-1] * n
    for i, j in enumerate(referral):
        if j != "-":
            temp[i] = idx[j]
    ans = [0] * n
    for s, a in zip(seller, amount):
        cur = idx[s]
        num = a * 100
        while cur != -1 and num > 0:
            x = num // 10
            y = num - x
            ans[cur] += y
            if x < 1:
                break
            cur = temp[cur]
            num = x
    return ans