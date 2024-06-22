def solution(arr):
    ans = 0
    while True:
        lst = []
        for x in arr:
            if x >= 50 and x % 2 == 0:
                lst.append(x // 2)
            elif x < 50 and x % 2 == 1:
                lst.append(x * 2 + 1)
            else:
                lst.append(x)
        if lst == arr:
            return ans
        arr = lst
        ans += 1