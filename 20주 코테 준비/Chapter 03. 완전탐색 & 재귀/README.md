### 완전탐색, 재귀

- 완전탐색 : 모든 경우의 수를 시도하는 방법, 입력이 작을 때 유효
- 백트래킹 : 재귀 탐색 중 조건이 맞지 않으면 되돌아가서 가지치기, 탐색 공간 감소
- 핵심 패턴
    - path에 추가 -> 재귀 -> path에서 제거(되돌리기)
    - 종료 조건을 먼저 정의
- sys.setrecursionlimit(100000) 반드시 추가

```python
import sys
from itertools import permutations, combinations, combinations_with_replacement

sys.setrecursionlimit(100000)


def backtrack(path, candidates, r):
    if len(path) == r:
        result.append(path[:])
        return
    for i, v in enumerate(candidates):
        if not used[i]:
            used[i] = True
            path.append(v)
            backtrack(path, candidates, r)
            path.pop()  # 되돌리기
            used[i] = False  # 되돌리기


list(permutations([1, 2, 3], 2))  # 순열
list(combinations([1, 2, 3], 2))  # 조합
list(combinations_with_replacement([1, 2, 3], 2))  # 중복조합
```