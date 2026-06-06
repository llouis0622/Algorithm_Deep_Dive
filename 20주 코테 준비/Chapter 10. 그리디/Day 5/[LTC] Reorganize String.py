from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        temp = Counter(s)
        if max(temp.values()) > (len(s) + 1) // 2:
            return ""
        heap = [(-cnt, char) for char, cnt in temp.items()]
        heapq.heapify(heap)
        res = []
        while len(heap) >= 2:
            cnt1, char1 = heapq.heappop(heap)
            cnt2, char2 = heapq.heappop(heap)
            res.append(char1)
            res.append(char2)
            if cnt1 + 1:
                heapq.heappush(heap, (cnt1 + 1, char1))
            if cnt2 + 1:
                heapq.heappush(heap, (cnt2 + 1, char2))
        if heap:
            res.append(heap[0][1])
        return ''.join(res)
