N, M = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = 0

for i in A:
    if start < i:
        start = i

    end += i

while start <= end:
    middle = int((start + end) / 2)
    sum = 0
    count = 0

    for i in range(N):
        if sum + A[i] > middle:
            count += 1
            sum = 0

        sum += A[i]

    if sum != 0:
        count += 1
    if count > M:
        start = middle + 1
    else:
        end = middle - 1

print(start)