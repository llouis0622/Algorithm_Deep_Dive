S = input()
if S.isupper():
    N = S.lower()
elif S.islower():
    N = S.upper()
else:
    N = S
print(f"{S}(ASCII: {ord(S)}) => {N}(ASCII: {ord(N)})")