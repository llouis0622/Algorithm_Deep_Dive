N = int(input())
L = list(map(int, input().split()))
X = int(input())
cnt = 0
for i in L:
    if i == X:
        cnt += 1
print(cnt)