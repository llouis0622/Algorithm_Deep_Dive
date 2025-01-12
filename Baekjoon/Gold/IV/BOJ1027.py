def building(n, height):
    num = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            visible = True
            temp = (height[j] - height[i]) / (j - i)
            for k in range(min(i, j) + 1, max(i, j)):
                if height[k] >= height[i] + temp * (k - i):
                    visible = False
                    break
            if visible:
                cnt += 1
        num = max(num, cnt)
    return num


n = int(input())
height = list(map(int, input().split()))
print(building(n, height))