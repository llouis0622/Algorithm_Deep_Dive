N = int(input())
temp = list(map(float, input().split()))
J = int(input())
C = int(input())
ans = temp[0]
tot = sum(temp)
for _ in range(C):
    p = ans / tot
    ans += p * J
    tot += J
print(ans)