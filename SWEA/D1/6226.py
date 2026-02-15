N = []
for i in range(1, 201):
    if i % 7 == 0 and i % 5 != 0:
        N.append(str(i))
print(','.join(N))