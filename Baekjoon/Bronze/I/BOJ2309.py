L = [int(input()) for _ in range(9)]
A, B = 0, 0
for i in range(9):
    for j in range(i+1, 9):
        if sum(L) - (L[i] + L[j]) == 100:
            A, B = L[i], L[j]
            break

L.remove(A)
L.remove(B)
L.sort()

for i in L:
    print(i)

# 난쟁이 키 전체 합에서 2명의 난쟁이 키를 빼서 100이 되도록 설계
# 이후 그 값을 전체 리스트에서 빼준 후 정렬하여 출력