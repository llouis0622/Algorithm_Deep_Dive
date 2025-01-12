def LCS(str1, str2):
    temp1, temp2 = len(str1), len(str2)
    DP = [[0] * (temp2 + 1) for _ in range(temp1 + 1)]
    for i in range(1, temp1 + 1):
        for j in range(1, temp2 + 1):
            if str1[i - 1] == str2[j - 1]:
                DP[i][j] = DP[i - 1][j - 1] + 1
            else:
                DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
    return DP[temp1][temp2]


str1 = input().strip()
str2 = input().strip()
print(LCS(str1, str2))