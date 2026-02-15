import random

N = random.randint(1, 9)
while True:
    S = input()
    if S == '종료':
        break
    S = int(S)
    if S == N:
        print("정답입니다!")
        break
    elif S > N:
        print(f"{S}보다 낮습니다!")
    else:
        print(f"{S}보다 높습니다!")