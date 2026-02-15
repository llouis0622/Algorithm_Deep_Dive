T = int(input())
for i in range(1, T + 1):
    S = input()
    if S.isupper():
        N = "대문자"
    else:
        N = "소문자"
    print(f"#{i} {S} 는 {N} 입니다.")