N = list(map(int, input().split(', ')))
print(*[i for i in N if i % 2 != 0], sep=', ')