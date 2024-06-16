def solution(num_list):
    ans = 0
    for i in num_list:
        while i > 1:
            if i % 2 == 0:
                i //= 2
            else:
                i = (i - 1) // 2
            ans += 1
    return ans