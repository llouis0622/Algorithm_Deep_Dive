num = (3, 5, 4, 1, 8, 10, 2)

m = num[0]
for i in num:
    if i > m:
        m = i

print(f"max{num} => {m}")