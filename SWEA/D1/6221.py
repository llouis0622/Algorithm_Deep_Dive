A = ["가위", "바위", "보"]
N = input()
M = input()
if N == M:
    print("Result : Draw")
elif (N == "가위" and M == "보") or (N == "바위" and M == "가위") or (N == "보" and M == "바위"):
    print("Result : Man1 Win!")
else:
    print("Result : Man2 Win!")