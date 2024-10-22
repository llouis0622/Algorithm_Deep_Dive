n = int(input())
cnt = 1
idx1, idx2 = 1, 1
sum = 1

while idx2 != n:
    if sum == n:
        cnt += 1
        idx2 += 1
        sum += idx2
    elif sum > n:
        sum -= idx1
        idx1 += 1
    else:
        idx2 += 1
        sum += idx2

print(cnt)