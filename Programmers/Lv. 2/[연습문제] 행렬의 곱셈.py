def solution(arr1, arr2):
    ans = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            total = 0
            for k in range(len(arr1[0])):
                total += arr1[i][k] * arr2[k][j]
            row.append(total)
        ans.append(row)
    return ans