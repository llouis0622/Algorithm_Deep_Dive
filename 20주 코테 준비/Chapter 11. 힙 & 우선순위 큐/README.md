### 힙 & 우선순위 큐

- 항상 최솟값(최댓값)을 O(log N)에 꺼낼 수 있는 완전 이진 트리
- Python heapq : 최소힙만 지원. 최대힙은 음수(-x)로 넣어서 구현
- 다익스트라 최단경로, 작업 스케줄링, 실시간 중앙값 유지

```python
import heapq

hq = []
heapq.heappush(hq, 5)
heapq.heappush(hq, 1)
top = hq[0]
val = heapq.heappop(hq)

heapq.heappush(hq, -5)
max_val = -heapq.heappop(hq)

heapq.heappush(hq, (1, 'task_a'))
p, task = heapq.heappop(hq)

heapq.nsmallest(3, arr)
heapq.nlargest(3, arr)
```