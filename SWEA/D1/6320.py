A = input()
B = input()
N = input()
M = input()
if N == '가위':
    if M == '가위':
        print('비겼습니다!')
    elif M == '바위':
        print('바위가 이겼습니다!')
    else:
        print('가위가 이겼습니다!')
elif N == '바위':
    if M == '가위':
        print('바위가 이겼습니다!')
    elif M == '바위':
        print('비겼습니다!')
    else:
        print('보가 이겼습니다!')
else:
    if M == '가위':
        print('가위가 이겼습니다!')
    elif M == '바위':
        print('보가 이겼습니다!')
    else:
        print('비겼습니다!')