T = int(input())
for i in range(1, T + 1):
    N = float(input())
    A = ""
    for _ in range(12):
        N *= 2
        if N >= 1:
            A += "1"
            N -= 1
        else:
            A += "0"
        if N == 0:
            break
    if N != 0:
        print(f"#{i} overflow")
    else:
        print(f"#{i} {A}")