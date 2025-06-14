s = input()
w = [1, 3] * 6
temp = s.index('*')
res = 0
for i in range(12):
    if i == temp:
        continue
    res += int(s[i]) * w[i]
num = int(s[-1])
for x in range(10):
    if (res + x * w[temp]) % 10 == (10 - num) % 10:
        print(x)
        break