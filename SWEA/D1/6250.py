score = {"가위": 1, "바위": 2, "보": 3}
while True:
    a = input()
    b = input()
    if score[a] == score[b]:
        print("무승부입니다.")
    elif (score[a] == 1 and score[b] == 3) or (score[a] == 2 and score[b] == 1) or (score[a] == 3 and score[b] == 2):
        print("Player A가 이겼습니다.")
    else:
        print("Player B가 이겼습니다.")
    print("게임을 계속 진행하겠습니까? (예/아니오)")
    if input() != "예":
        break