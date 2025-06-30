import heapq


def minute(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m


def solution(book_time):
    temp = []
    for s, e in book_time:
        start = minute(s)
        end = minute(e) + 10
        temp.append((start, end))
    temp.sort()
    heap = []
    for start, end in temp:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)