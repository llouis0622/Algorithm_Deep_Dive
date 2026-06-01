### 그리디 알고리즘

- 매 순간 최적 선택 -> 전체 최적. 탐욕 선택이 최적임을 보장할 수 있는 구조에서만 사용
- 핵심 패턴
  - 회의실 배정 : 끝나는 시간 기준 정렬
  - 거스름돈 : 큰 단위부터
  - 구명보트 : 정렬 후 투 포인터
- 그리디가 맞는지 확인 : 반례 찾기. 반례 미존재시 그리디

```python
def meeting(meetings):
    meetings.sort(key=lambda x: (x[1], x[0]))
    cnt, end = 0, 0
    for s, e in meetings:
        if s >= end:
            cnt += 1
            end = e
    return cnt


def lifeboat(people, limit):
    people.sort()
    lo, hi = 0, len(people) - 1
    cnt = 0
    while lo <= hi:
        if people[lo] + people[hi] <= limit:
            lo += 1
        hi -= 1
        cnt += 1
    return cnt
```