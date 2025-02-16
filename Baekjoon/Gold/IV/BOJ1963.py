from collections import deque


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def BFS(s, t):
    if s == t:
        return 0
    queue = deque([(s, 0)])
    visited = set([s])
    while queue:
        num, steps = queue.popleft()
        for n in check(num):
            if n == t:
                return steps + 1
            if n not in visited:
                visited.add(n)
                queue.append((n, steps + 1))
    return "Impossible"


def check(num):
    temp = []
    num = str(num)
    for i in range(4):
        for d in range(10):
            if d != int(num[i]):
                new = int(num[:i] + str(d) + num[i + 1:])
                if new >= 1000 and is_prime(new):
                    temp.append(new)
    return temp


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(BFS(A, B))