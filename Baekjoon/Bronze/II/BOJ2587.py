L = [int(input()) for _ in range(5)]
L.sort()
print(sum(L) // len(L), L[2], sep='\n')