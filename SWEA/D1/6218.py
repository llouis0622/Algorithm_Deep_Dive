N = int(input())
for i in range(1, N + 1):
    if N % i == 0:
        print(f"{i}(은)는 {N}의 약수입니다.")