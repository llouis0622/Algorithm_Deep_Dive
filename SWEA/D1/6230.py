N = [88, 30, 61, 55, 95]
for i in range(len(N)):
    if N[i] >= 60:
        print(f"{i + 1}번 학생은 {N[i]}점으로 합격입니다.")
    else:
        print(f"{i + 1}번 학생은 {N[i]}점으로 불합격입니다.")