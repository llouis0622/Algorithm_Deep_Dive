S = input().strip()
A = [str(ord(i) - ord('A') + 1) for i in S]
print(' '.join(A))