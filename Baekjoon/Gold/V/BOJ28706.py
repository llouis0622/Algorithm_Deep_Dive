import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    check = [False] * 7
    check[1] = True
    for _ in range(N):
        op1, v1, op2, v2 = input().split()
        v1 = int(v1)
        v2 = int(v2)
        temp = [False] * 7
        for r in range(7):
            if check[r]:
                if op1 == '+':
                    temp[(r + v1) % 7] = True
                else:
                    temp[(r * v1) % 7] = True
                if op2 == '+':
                    temp[(r + v2) % 7] = True
                else:
                    temp[(r * v2) % 7] = True
        check = temp
    print("LUCKY" if check[0] else "UNLUCKY")