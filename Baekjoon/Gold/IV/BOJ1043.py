N, M = map(int, input().split())
trueP = list(map(int, input().split()))
T = trueP[0]
del trueP[0]
result = 0
party = [[] for _ in range(M)]


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a


def checkSame(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return True
    return False


for i in range(M):
    party[i] = list(map(int, input().split()))
    del party[i][0]

parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

for i in range(M):
    firstPeople = party[i][0]

    for j in range(1, len(party[i])):
        union(firstPeople, party[i][j])

for i in range(M):
    isPossible = True
    cur = party[i][0]

    for j in range(len(trueP)):
        if find(cur) == find(trueP[j]):
            isPossible = False
            break

    if isPossible:
        result += 1

print(result)