S = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
N = 0
while S:
    A = S.pop()
    if A >= 80:
        N += A
print(N)