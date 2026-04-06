### 딕셔너리, 셋, 정렬

- 딕셔너리 : 해시맵, 탐색/삽입/삭제 모두 평균 O(1)
- 셋 : 중복 없는 해시 집합, 'x in set'은 O(1), 'x in list'는 O(N)
- 정렬 : sorted()는 새 리스트 반환, list.sort()는 제자리 정렬, key 함수로 기준 지정
- 다중 기준 정렬 -> 튜플로 key=lambda x: (x[1], -x[0])

```python
from collections import defaultdict, Counter
from functools import cmp_to_key

freq = defaultdict(int)
for x in arr:
    freq[x] += 1

c = Counter('mississippi')
c.most_common(3)

seen = set()
for x in arr:
    if x in seen:
        print('중복!')
    seen.add(x)

arr.sort(key=lambda x: (x[1], -x[0]))


def cmp(a, b):
    if a + b > b + a:
        return -1
    return 1


nums.sort(key=cmp_to_key(cmp))
```