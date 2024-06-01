def solution(arr):
    ans = []

    for i in arr:
        if i >= 50 and i % 2 == 0:
            ans.append(i // 2)
        elif i < 50 and i % 2 == 1:
            ans.append(i * 2)
        else:
            ans.append(i)

    return ans