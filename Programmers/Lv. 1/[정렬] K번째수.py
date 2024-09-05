def solution(array, commands):
    ans = []
    for idx in commands:
        i, j, k = idx
        arr = sorted(array[i - 1:j])
        ans.append(arr[k - 1])
    return ans