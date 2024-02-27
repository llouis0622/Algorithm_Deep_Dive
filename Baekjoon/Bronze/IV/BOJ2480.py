A, B, C = map(int, input().split())
if A == B == C:
    print(A * 1000 + 10000)
elif A == B != C:
    print(A * 100 + 1000)
elif B == C != A:
    print(B * 100 + 1000)
elif C == A != B:
    print(C * 100 + 1000)
else:
    print(max(A, B, C) * 100)