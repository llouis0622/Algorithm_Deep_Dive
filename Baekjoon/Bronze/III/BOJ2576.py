O = []
for _ in range(7):
    N = int(input())
    if N % 2:
        O.append(N)
if len(O) == 0:
    print(-1)
else:
    print(sum(O))
    print(min(O))