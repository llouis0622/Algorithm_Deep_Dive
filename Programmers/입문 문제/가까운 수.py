def solution(array, n):
    ans = array[0]
    for i in array:
        if abs(i - n) < abs(ans - n) or (abs(i - n) == abs(ans - n) and i < ans):
            ans = i
    return ans