from itertools import combinations


def nums():
    num = []
    for l in range(1, 11):
        for c in combinations(range(10), l):
            num.append(int("".join(map(str, sorted(c, reverse=True)))))
    return sorted(num)


def find(n):
    temp = nums()
    return temp[n] if n < len(temp) else -1


n = int(input())
print(find(n))