N = []
for _ in range(5):
    N.append(int(input()))
print(f'입력된 값 {N}의 평균은 {sum(N) / len(N):.1f}입니다.')