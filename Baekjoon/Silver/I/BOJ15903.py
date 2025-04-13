import heapq

N, M = map(int, input().split())
card = list(map(int, input().split()))
heapq.heapify(card)
for _ in range(M):
    x = heapq.heappop(card)
    y = heapq.heappop(card)
    temp = x + y
    heapq.heappush(card, temp)
    heapq.heappush(card, temp)
print(sum(card))