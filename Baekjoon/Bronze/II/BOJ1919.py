A = input()
B = input()
cnt = 0
for i in range(97, 123):
    cnt += abs(A.count(chr(i)) - B.count(chr(i)))
print(cnt)