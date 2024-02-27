A, B = map(int, input().split())
start, end = min(A, B), max(A, B)
cnt = max(end - start - 1, 0)
print(cnt)
if cnt > 0:
    for i in range(start + 1, end):
        print(i, end=' ')