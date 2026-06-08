import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    ans = 0
    while len(scoville) >= 2 and scoville[0] < K:
        num = heapq.heappop(scoville)
        tot = heapq.heappop(scoville)
        heapq.heappush(scoville, num + tot * 2)
        ans += 1
    return ans if scoville[0] >= K else -1
