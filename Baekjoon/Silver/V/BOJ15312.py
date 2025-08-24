import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
temp = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
ans = []
for i in range(len(A)):
    ans.append(temp[ord(A[i]) - 65])
    ans.append(temp[ord(B[i]) - 65])
while len(ans) > 2:
    ans = [(ans[i] + ans[i + 1]) % 10 for i in range(len(ans) - 1)]
print(f"{ans[0]}{ans[1]}")