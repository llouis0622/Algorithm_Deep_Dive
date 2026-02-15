S = input()
A, B = S.split("://", 1)
if "/" in B:
    X, Y = B.split("/", 1)
else:
    X = B
    Y = ""
print(f"protocol: {A}")
print(f"host: {X}")
print(f"others: {Y}")