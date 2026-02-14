S = list(map(str, input().split(', ')))
S.sort()
print(*S, sep=', ')