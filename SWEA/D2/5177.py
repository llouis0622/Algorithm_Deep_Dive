T = int(input())
for i in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    heap = [0] * (N + 1)
    size = 0
    for j in A:
        size += 1
        heap[size] = j
        a = size
        while a > 1 and heap[a] < heap[a // 2]:
            heap[a], heap[a // 2] = heap[a // 2], heap[a]
            a //= 2
    res = 0
    a = N
    while a > 1:
        a //= 2
        res += heap[a]
    print(f"#{i} {res}")