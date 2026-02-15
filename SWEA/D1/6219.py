N = int(input())
A = []
for i in range(1, N + 1):
    if N % i == 0:
        A.append(i)
        print(f"{i}(은)는 {N}의 약수입니다.")
if len(A) == 2:
    print(f"{N}(은)는 1과 {N}로만 나눌 수 있는 소수입니다.")