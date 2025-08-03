## 1️⃣ 이분 탐색

- 정렬되어 있는 배열에서 특정 데이터를 찾기 위해 모든 데이터를 순차적으로 확인하는 대신 탐색 범위를 절반으로 줄여가며 찾는 탐색 방법

### Parametric Search(매개 변수 탐색)

- 조건을 만족하는 최소/최대값을 구하는 문제(최적화 문제)를 결정 문제로 변환해 이분 탐색을 수행하는 방법

## 2️⃣ 이분 탐색 풀이 방법

### **이분 탐색 선택 가능성**

- 정답이 특정 범위(1~1e9)에 있는가
- 정렬된 자료에서 특정 값을 찾는가
- 조건을 만족하는 가장 작은/큰 값이 정답인가
- 완전 탐색하면 시간초과가 나는가

### **이분 탐색 문제 판별법**

- 정렬된 배열에서 특정 값 찾기 → 기본 이분 탐색
- 조건을 만족하는 최소/최대 값 찾기 → 기본 이분 탐색 + 다른 알고리즘
- 완전 탐색 시 시간 초과 → 이분 탐색으로 최적화
- 정답이 수치 범위 안에 존재 → Parametric Search

### **이분 탐색 풀이 기본 흐름**

- 탐색할 범위 정의 - 보통 입력에서 정답의 최소값/최대값 유추 후 범위 설정
- 정답 조건 판단 함수 - mid 값이 정답이 될 수 있는지 판단 & 논리적으로 해석
- 이분 탐색 루프 작성 - while 문 or for 문으로 작성 후 탐색 시작
- 정답 출력 - 문제 조건에 따라 다르게 처리

## 3️⃣ 수업 코드

### BOJ1920: 수 찾기

```python
import sys

input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

def binary_search(arr, target):
    st, en = 0, len(arr) - 1
    while st <= en:
        mid = (st + en) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            st = mid + 1
        else:
            en = mid - 1
    return 0

for x in targets:
    print(binary_search(a, x))
```

```python
import sys

input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
for x in targets:
    print(1 if x in A else 0)
```

```java
import java.io.*;
import java.util.*;

public class Main {

    static int[] a;
    static int n;

    public static int binarySearch(int target) {
        int st = 0;
        int en = n - 1;
        while (st <= en) {
            int mid = (st + en) / 2;
            if (a[mid] < target) st = mid + 1;
            else if (a[mid] > target) en = mid - 1;
            else return 1;
        }
        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        a = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(a);

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int t = Integer.parseInt(st.nextToken());
            sb.append(binarySearch(t)).append('\n');
        }

        System.out.print(sb);
    }
}
```

### BOJ10816: 숫자 카드 2

```python
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
targets = list(map(int, input().split()))
for t in targets:
    lower = bisect_left(a, t)
    upper = bisect_right(a, t)
    print(upper - lower)
```

```python
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
counter = Counter(cards)
m = int(input())
targets = list(map(int, input().split()))
print(' '.join(str(counter[t]) for t in targets))
```

```java
import java.io.*;
import java.util.*;

public class Main {

    static int[] a;

    static int lowerBound(int[] arr, int target) {
        int st = 0, en = arr.length;
        while (st < en) {
            int mid = (st + en) / 2;
            if (arr[mid] >= target) en = mid;
            else st = mid + 1;
        }
        return st;
    }

    static int upperBound(int[] arr, int target) {
        int st = 0, en = arr.length;
        while (st < en) {
            int mid = (st + en) / 2;
            if (arr[mid] > target) en = mid;
            else st = mid + 1;
        }
        return st;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        a = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(a);

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            int t = Integer.parseInt(st.nextToken());
            int lower = lowerBound(a, t);
            int upper = upperBound(a, t);
            sb.append(upper - lower).append(' ');
        }

        System.out.println(sb);
    }
}
```

### BOJ18870: 좌표 압축

```python
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
temp = sorted(set(arr))
num = {v: i for i, v in enumerate(temp)}
print(' '.join(str(num[x]) for x in arr))
```

```java
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] x = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) x[i] = Integer.parseInt(st.nextToken());

        Set<Integer> set = new TreeSet<>();
        for (int val : x) set.add(val);

        Map<Integer, Integer> map = new HashMap<>();
        int idx = 0;
        for (int val : set) map.put(val, idx++);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) sb.append(map.get(x[i])).append(' ');
        System.out.println(sb);
    }
}
```

### BOJ2295: 세 수의 합

```python
import sys

input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()
two = []
for i in range(n):
    for j in range(i, n):
        two.append(a[i] + a[j])
two.sort()
for i in range(n - 1, 0, -1):
    for j in range(i):
        target = a[i] - a[j]
        left, right = 0, len(two) - 1
        while left <= right:
            mid = (left + right) // 2
            if two[mid] == target:
                print(a[i])
                sys.exit()
            elif two[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
```

```python
import sys

input = sys.stdin.readline

n = int(input())
U = [int(input()) for _ in range(n)]
U.sort()
num = set()
for i in range(n):
    for j in range(n):
        num.add(U[i] + U[j])
for k in range(n - 1, -1, -1):
    for l in range(n):
        if (U[k] - U[l]) in num:
            print(U[k])
            exit()
```

```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(br.readLine());

        Arrays.sort(a);

        ArrayList<Integer> two = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                two.add(a[i] + a[j]);
            }
        }
        Collections.sort(two);

        for (int i = n - 1; i > 0; i--) {
            for (int j = 0; j < i; j++) {
                int target = a[i] - a[j];
                int idx = Collections.binarySearch(two, target);
                if (idx >= 0) {
                    System.out.println(a[i]);
                    return;
                }
            }
        }
    }
}
```

### BOJ1654: 랜선 자르기

```python
import sys

input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

def solve(x):
    return sum(a // x for a in arr) >= n

st, en = 1, 2 ** 31 - 1
while st < en:
    mid = (st + en + 1) // 2
    if solve(mid):
        st = mid
    else:
        en = mid - 1
print(st)
```

```java
import java.io.*;
import java.util.*;

public class Main {
    static int k, n;
    static int[] arr;

    static boolean solve(long x) {
        long count = 0;
        for (int i = 0; i < k; i++) count += arr[i] / x;
        return count >= n;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stz = new StringTokenizer(br.readLine());
        k = Integer.parseInt(stz.nextToken());
        n = Integer.parseInt(stz.nextToken());
        arr = new int[k];
        for (int i = 0; i < k; i++) arr[i] = Integer.parseInt(br.readLine());

        long st = 1, en = (1L << 31) - 1;
        while (st < en) {
            long mid = (st + en + 1) / 2;
            if (solve(mid)) st = mid;
            else en = mid - 1;
        }
        System.out.println(st);
    }
}
```