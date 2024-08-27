def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr1[0])
    ans = []
    for i in range(row):
        arr = []
        for j in range(col):
            arr.append(arr1[i][j] + arr2[i][j])
        ans.append(arr)
    return ans