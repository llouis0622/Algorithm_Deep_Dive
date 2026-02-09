N = int(input())
num = [0] * 10
for i in range(10):
    print(i, end=' ')
print()
for i in str(N):
    num[int(i)] += 1
print(*num, end=' ')