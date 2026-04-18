def solution(s):
    if len(s) == 1:
        return 1
    ans = len(s)
    for i in range(1, len(s) // 2 + 1):
        prev = s[:i]
        cnt = 1
        temp = ''
        for x in range(i, len(s), i):
            cur = s[x:x + i]
            if prev == cur:
                cnt += 1
            else:
                if cnt > 1:
                    temp += str(cnt) + prev
                else:
                    temp += prev
                prev = cur
                cnt = 1
        if cnt > 1:
            temp += str(cnt) + prev
        else:
            temp += prev
        ans = min(ans, len(temp))
    return ans
