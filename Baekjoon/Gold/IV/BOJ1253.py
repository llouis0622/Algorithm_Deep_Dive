import sys

input = sys.stdin.readline
N = int(input())
res = 0

lst = list(map(int, input().split()))
lst.sort()

for i in range(N):
    idx = lst[i]
    i = int(0)
    j = int(N - 1)
    
    while i < j:
        if lst[i] + lst[j] == idx:
            if i != i and j != i:
                res += 1
                break
            elif i == i:
                i += 1
            elif j == i:
                j -= 1
        elif lst[i] + lst[j] < idx:
            i += 1
        else:
            j -= 1

print(res)