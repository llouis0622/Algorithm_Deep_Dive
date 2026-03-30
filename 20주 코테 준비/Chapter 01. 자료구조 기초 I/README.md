### 스택, 큐, 덱

- 스택 : 나중에 넣은 게 먼저 나오는 LIFO 구조, Python list로 구현하고 append/pop 사용
- 큐 : 먼저 넣은 게 먼저 나오는 FIFO 구조, collections.deque 사용
- 덱 : 앞뒤 양쪽으로 O(1) 삽입/삭제, 슬라이딩 윈도우 최적화에 자주 씀

```python
from collections import deque

stack = []
stack.append(1)
stack.append(2)
top = stack[-1] # peek
stack.pop() # O(1)

q = deque()
q.append(1)
q.append(2)
front = q[0] # peek
q.popleft() # O(1)

dq = deque([1, 2, 3])
dq.appendleft(0) # 왼쪽 추가
dq.popleft() # 왼쪽 제거
dq.rotate(1) # 오른쪽으로 1칸 회전
```