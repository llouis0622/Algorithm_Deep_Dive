## 1️⃣ 백트래킹(Backtracking)

### 백트래킹이란?

- 현재 상태에서 가능한 모든 후보군을 따라 들어가며 탐색하는 알고리즘

## 2️⃣ 백트래킹 풀이 방법

### **백트래킹 선택 가능성**

- 조건이 안 맞으면 즉시 멈춰야 효율적인가?
- 가능한 선택지가 여러 갈래로 나눠지는가?
- 모든 경우의 수 중에서 특정 조건 만족 해만 찾는가?
- 완전 탐색은 너무 오래 걸릴 수 있는가?
- 위 질문을 만족하면 백트래킹

### **백트래킹 문제 판별법**

- 모든 경우의 수 → 조건에 맞는 것만 찾아야 함 : N-Queen, 부분집합
- DFS로 모든 경로 탐색 : 경로 찾기, 순열 생성
- 조합, 순열, 부분집합 생성 : M개의 수 고르기
- 경우의 수가 폭발적으로 많음 : 가지치기 없으면 시간초과 발생 문제

### **백트래킹 풀이 기본 흐름**

- 탐색 시작 - 어떤 선택지부터 시작할지 판별
- 조건 체크 - 불가능하면 즉시 return
- 유망하다면 진행 - 선택 후 다음 단계로
- 완료되면 정답 처리 - 결과 저장 및 출력
- 원상복구 - 선택 이전 상태로 돌려놓기

## 3️⃣ 실습 코드

### BOJ15649: N과 M (1)

```python
n, m = map(int, input("n m 입력: ").split())
arr = [0] * 10
isused = [False] * 10

def func(k, depth=0):
    indent = '  ' * depth
    if k == m:
        print(f"{indent} 정답 도출 : {arr[:m]}")
        return
    for i in range(1, n + 1):
        if not isused[i]:
            print(f"{indent}+ {k + 1}번째에 {i} 선택")
            arr[k] = i
            isused[i] = True
            func(k + 1, depth + 1)
            print(f"{indent}- {k + 1}번째에서 {i} 되돌리기 (백트래킹)")
            isused[i] = False

func(0)
```

```python
n, m = map(int, input().split())
arr = [0] * 10
isused = [False] * 10

def func(k):  # 현재 k개까지 수를 택했음
    if k == m:  # m개 모두 택했으면 출력
        print(*arr[:m])
        return
    for i in range(1, n + 1):
        if not isused[i]:  # 아직 사용되지 않았다면
            arr[k] = i  # k번째 수를 i로 정함
            isused[i] = True  # i를 사용되었다고 표시
            func(k + 1)  # 다음 수를 정하러 감
            isused[i] = False  # i 사용 해제

func(0)
```

```java
import java.util.Scanner;

public class Main {
    static int n, m;
    static int[] arr = new int[10];
    static boolean[] isused = new boolean[10];

    static void func(int k) { // 현재 k개까지 수를 택했음
        if (k == m) { // m개 모두 택했으면 출력
            for (int i = 0; i < m; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 1; i <= n; i++) { // 1부터 n까지
            if (!isused[i]) { // 사용되지 않았다면
                arr[k] = i; // k번째 수를 i로 정함
                isused[i] = true; // i 사용
                func(k + 1); // 다음 수 선택
                isused[i] = false; // i 사용 해제
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        func(0);
    }
}
```

### BOJ9663: N-Queen

```python
n = int(input("체스판 크기 n 입력: "))
cnt = 0
isused1 = [False] * n  # 열 점유 여부
isused2 = [False] * (2 * n - 1)  # / 방향 대각선 (r + c)
isused3 = [False] * (2 * n - 1)  # \ 방향 대각선 (r - c + n - 1)

def func(cur, depth=0):  # cur행에 퀸을 놓는 함수
    global cnt
    indent = '  ' * depth
    if cur == n:
        cnt += 1
        print(f"{indent}✅ 퀸 {n}개 배치 성공! 현재 경우의 수 : {cnt}")
        return
    for i in range(n):  # (cur행, i열)에 퀸 놓을 수 있는지 검사
        if isused1[i] or isused2[cur + i] or isused3[cur - i + n - 1]:
            print(f"{indent}✖️ 위치 ({cur},{i})는 위협받음! 건너뜀")
            continue
        print(f"{indent}✔️ 위치 ({cur},{i})에 퀸 배치 시도")
        isused1[i] = isused2[cur + i] = isused3[cur - i + n - 1] = True
        func(cur + 1, depth + 1)
        print(f"{indent}↩️ 위치 ({cur},{i}) 퀸 제거 (백트래킹)")
        isused1[i] = isused2[cur + i] = isused3[cur - i + n - 1] = False

func(0)
print(f"\n총 경우의 수 : {cnt}")
```

```python
n = int(input())
cnt = 0
isused1 = [False] * n  # column 점유 여부
isused2 = [False] * (2 * n - 1)  # / 방향 대각선 점유 여부
isused3 = [False] * (2 * n - 1)  # \ 방향 대각선 점유 여부

def func(cur):  # cur번째 row에 배치 예정
    global cnt
    if cur == n:
        cnt += 1
        return
    for i in range(n):  # (cur, i)에 배치 시도
        if isused1[i] or isused2[i + cur] or isused3[cur - i + n - 1]:
            continue
        isused1[i] = isused2[i + cur] = isused3[cur - i + n - 1] = True
        func(cur + 1)
        isused1[i] = isused2[i + cur] = isused3[cur - i + n - 1] = False

func(0)
print(cnt)
```

```java
import java.util.Scanner;

public class Main {
    static boolean[] isused1; // column
    static boolean[] isused2; // /
    static boolean[] isused3; // \
    static int cnt = 0;
    static int n;

    static void func(int cur) {
        if (cur == n) {
            cnt++;
            return;
        }

        for (int i = 0; i < n; i++) {
            if (isused1[i] || isused2[i + cur] || isused3[cur - i + n - 1]) continue;
            isused1[i] = isused2[i + cur] = isused3[cur - i + n - 1] = true;
            func(cur + 1);
            isused1[i] = isused2[i + cur] = isused3[cur - i + n - 1] = false;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        isused1 = new boolean[n];
        isused2 = new boolean[2 * n - 1];
        isused3 = new boolean[2 * n - 1];

        func(0);
        System.out.println(cnt);
    }
}
```

### BOJ1182: 부분수열의 합

```python
n, s = map(int, input("n s 입력: ").split())
arr = list(map(int, input("배열 입력: ").split()))
cnt = 0

def func(cur, total, depth=0):
    global cnt
    indent = '  ' * depth
    if cur == n:
        if total == s:
            print(f"{indent}🎯 total = {total}, 목표 달성! +1")
            cnt += 1
        else:
            print(f"{indent}🔸 total = {total}, 목표 아님")
        return
    # 현재 원소 포함하는 경우
    print(f"{indent}+ {arr[cur]} 포함 → 다음으로")
    func(cur + 1, total + arr[cur], depth + 1)
    # 현재 원소 포함하지 않는 경우
    print(f"{indent}- {arr[cur]} 제외 → 다음으로")
    func(cur + 1, total, depth + 1)

func(0, 0)
# 공집합의 합도 0이므로 s가 0이면 그 경우 제외
if s == 0:
    cnt -= 1
print(f"\n총 경우의 수 : {cnt}")
```

```python
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def func(cur, total):
    global cnt
    if cur == n:
        if total == s and total != 0:
            cnt += 1
        return
    func(cur + 1, total + arr[cur])  # 포함
    func(cur + 1, total)  # 미포함

func(0, 0)
# 공집합 제외 조건 : S가 0이면 아무것도 선택 안 한 경우 포함되므로 제외
if s == 0:
    cnt -= 1
print(cnt)
```

```java
import java.util.Scanner;

public class Main {
    static int n, s;
    static int[] arr;
    static int cnt = 0;

    static void func(int cur, int total) {
        if (cur == n) {
            if (total == s) cnt++;
            return;
        }

        func(cur + 1, total + arr[cur]); // 포함
        func(cur + 1, total);            // 미포함
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        s = sc.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        func(0, 0);

        if (s == 0) cnt--; // 공집합 제외

        System.out.println(cnt);
    }
}
```