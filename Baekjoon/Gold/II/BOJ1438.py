import sys

input = sys.stdin.readline
N = int(input().strip())
points = [tuple(map(int, input().split())) for _ in range(N)]
points.sort(key=lambda p: p[0])
M = N // 2
ans = float('inf')
for i in range(N):
    for j in range(i, N):
        K = j - i + 1
        if K < M:
            continue
        num = [points[k][1] for k in range(i, j + 1)]
        num.sort()
        width = points[j][0] - points[i][0] + 2
        for k in range(0, K - M + 1):
            height = num[k + M - 1] - num[k] + 2
            area = width * height
            if area < ans:
                ans = area
print(ans)