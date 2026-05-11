### 이분탐색 & Parametric Search

- 정렬된 배열에서 O(log N)으로 탐색
- Parametric Search : '값 x가 조건을 만족하는가'로 치환해서 최적값 탐색
  - 최댓값의 최솟값 구하기 -> lo 올리기
  - 최솟값의 최댓값 구하기 -> hi 내리기
- bisect 모듈 : bisect_left(target 이상 첫 위치), bisect_right(target 초과 첫 위치)

```python
import bisect


def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def parametric_max(lo, hi):
    ans = 0
    while lo <= hi:
        mid = (lo + hi) / 2
        if check(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


bisect.bisect_left(arr, 4)
bisect.bisect_right(arr, 4)
```