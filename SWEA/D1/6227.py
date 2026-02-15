N = []
for i in range(100, 301):
    s = str(i)
    if all(int(d) % 2 == 0 for d in s):
        N.append(s)
print(','.join(N))