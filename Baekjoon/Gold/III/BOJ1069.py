import math

X, Y, D, T = map(int, input().split())
temp = math.hypot(X, Y)
ans1 = temp
num = 0
N = 0
while num <= temp:
    num += D
    N += 1
N -= 1
num -= D
ans2 = max(T * (N + 1), 2 * T)
ans3 = T * N + (temp - D * N)
ans4 = T * (N + 1) + (D * (N + 1) - temp)
print(f"{min(min(ans1, ans2), min(ans3, ans4)):.16f}")