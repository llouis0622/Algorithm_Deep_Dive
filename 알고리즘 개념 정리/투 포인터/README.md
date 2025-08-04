## 1️⃣ 투 포인터

- 배열에서 원래 이중 for문으로 O(N^2)에 처리되는 작업을 2개의 포인터의 움직임으로 O(N)에 해결하는 알고리즘

## 2️⃣ 투 포인터 풀이 방법

### **투 포인터 선택 가능성**

- 배열이 정렬되어 있음 → 투 포인터 적용 가능
- 연속된 구간(부분 수열)을 다룸 → 슬라이딩 윈도우 or 투 포인터
- 부분합, 조건을 만족하는 쌍 찾기 → 투 포인터 가능성 매우 높음
- 시간 제한이 빠듯함 & 완전탐색 시 O(N2) 이상 → 투 포인터

### **투 포인터 문제 판별법**

- 정렬된 수열 + 합 조건
- 두 수의 차이/합
- 특정 구간(구간합, 연속된 원소)의 조건 만족 여부
- 최소 길이/최대 길이/개수 세기
- 정렬된 배열에서 두 개를 골라 어떤 조건을 만족하는 쌍을 구함

### **투 포인터 풀이 기본 흐름**

- 두 개의 포인터를 배열의 양 끝 또는 시작점에 둠
- 조건 만족 – 한쪽 포인터를 움직이며 결과 갱신
- 조건 불만족 – 다른 쪽 포인터를 움직이며 보정

## 3️⃣ 수업 코드

### BOJ2230: 수 고르기

```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(int(input()) for _ in range(n))
res = int(1e10)
en = 0
for st in range(n):
    while en < n and a[en] - a[st] < m:
        en += 1
    if en == n:
        break
    res = min(res, a[en] - a[st])
print(res)
```

```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stz = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stz.nextToken());
        int m = Integer.parseInt(stz.nextToken());

        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(br.readLine());
        Arrays.sort(a);

        int res = Integer.MAX_VALUE;
        int en = 0;

        for (int st = 0; st < n; st++) {
            while (en < n && a[en] - a[st] < m) en++;
            if (en == n) break;
            res = Math.min(res, a[en] - a[st]);
        }

        System.out.println(res);
    }
}
```

### BOJ1806: 부분합

```python
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))
tot = a[0]
en = 0
res = int(1e9)
for st in range(n):
    while en < n and tot < s:
        en += 1
        if en != n:
            tot += a[en]
    if en == n:
        break
    res = min(res, en - st + 1)
    tot -= a[st]
print(0 if res == int(1e9) else res)
```

```python
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))
st, en, tot = 0, 0, 0
res = int(1e9)
while True:
    if tot >= s:
        res = min(res, en - st)
        tot -= a[st]
        st += 1
    elif en == n:
        break
    else:
        tot += a[en]
        en += 1
print(res if res != int(1e9) else 0)
```

```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stz = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stz.nextToken());
        int s = Integer.parseInt(stz.nextToken());

        int[] a = new int[n];
        stz = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(stz.nextToken());

        int tot = a[0], en = 0, res = Integer.MAX_VALUE;

        for (int st = 0; st < n; st++) {
            while (en < n && tot < s) {
                en++;
                if (en != n) tot += a[en];
            }
            if (en == n) break;
            res = Math.min(res, en - st + 1);
            tot -= a[st];
        }

        System.out.println(res == Integer.MAX_VALUE ? 0 : res);
    }
}
```