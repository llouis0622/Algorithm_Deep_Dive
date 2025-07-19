## 1️⃣ 재귀(Recursion)

### 재귀란?

- 하나의 함수에서 자기 자신을 다시 호출해 작업을 수행하는 알고리즘

### 수학적 귀납법

- 어떤 명제가 모든 자연수에 대해 참임을 증명하는 방법
- 가장 작은 수에 대해 성립함을 보여줌
- n=k일 때 성립한다고 가정 → n=k+1일 때도 성립함을 보임

### 재귀 함수의 조건

- 특정 입력에 대해서는 자기 자신을 호출하지 않고 종료되어야 함
- 모든 입력은 base condition으로 수렴해야 함

### 재귀에 대한 정보

- 함수의 인자로 어떤 것을 받고 어디까지 계산한 후 자기 자신에게 넘겨줄지 명확하게 정해야 함
- 모든 재귀 함수는 반복문만으로 동일한 동작을 하는 함수를 만들 수 있음
- 재귀는 반복문으로 구현했을 때에 비해 코드가 간결하지만 메모리/시간에서는 손해
- 한 함수가 자기 자신을 여러 번 호출하게 되면 비효율적

## 2️⃣ 재귀 풀이 방법

### **재귀 선택 가능성**

- 문제 구조가 트리/그래프 탐색이면? → DFS로 재귀 거의 필수
- 분할 정복이면? → 재귀가 깔끔(퀵정렬, 병합정렬, 하노이 등)
- 백트래킹이면? → 재귀 패턴 거의 100%
- 문제에 반복되는 패턴이 계층적으로 쌓여 있다면? → 재귀로 흐름 단순
- 반복문으로 가능하지만 코드가 복잡해질 때 → 재귀로 단순화 가능

### **재귀 문제 판별법**

- 동일한 로직이 단계별로 반복 : 팩토리얼, 피보나치
- 큰 문제 = 동일한 구조의 작은 문제 + 연산 : 하노이, 분할 정복
- 선택과 되돌아감이 필요 : N-Queen, 부분집합
- 트리 구조, 그래프 탐색 : DFS
- 순서를 스택처럼 유지 : DFS

### **재귀 풀이 기본 흐름**

- 기저 조건 찾기 - 무한 루프 방지 & 종료 조건 확실
- 점화식 확인 - 큰 문제 → 작은 문제로 쪼갤 수 있는지 & 결과를 어떻게 결합할지
- 호출 흐름 디버깅 - 작은 입력으로 흐름 확인 & 예상과 다르면 점화식부터 의심
- 스택 깊이 한계 고려 - 필요시 sys.setrecursionlimit() 사용

## 3️⃣ 수업 코드

### BOJ1629: 곱셈

```python
def fast_pow(a, b, c, depth=0):
    indent = '  ' * depth
    if b == 1:
        print(f"{indent}기저 조건 도달 : {a}^{b} mod {c} = {a % c}")
        return a % c
    print(f"{indent}{a}^{b} mod {c} 계산 중... b = {b} -> b // 2 = {b // 2}")
    half = fast_pow(a, b // 2, c, depth + 1)
    if b % 2 == 0:
        result = (half * half) % c
        print(f"{indent}b가 짝수 → {half} * {half} mod {c} = {result}")
    else:
        result = (half * half * a) % c
        print(f"{indent}b가 홀수 → {half} * {half} * {a} mod {c} = {result}")
    return result

a, b, c = map(int, input("a, b, c를 공백으로 입력하세요 : ").split())
print(f"\n최종 결과 : {a}^{b} mod {c} = {fast_pow(a, b, c)}")
```

```python
def fast_pow(a, b, c):
    if b == 1:
        return a % c
    num = fast_pow(a, b // 2, c)
    if b % 2 == 0:
        return (num * num) % c
    else:
        return (num * num * a) % c

a, b, c = map(int, input().split())
print(fast_pow(a, b, c))
```

```java
import java.util.Scanner;

public class Main {
    static long fastPow(long a, long b, long c) {
        if (b == 1) return a % c;

        long num = fastPow(a, b / 2, c);

        if (b % 2 == 0) return (num * num) % c;
        else return (num * num % c) * a % c;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long a = sc.nextLong();
        long b = sc.nextLong();
        long c = sc.nextLong();

        System.out.println(fastPow(a, b, c));
    }
}
```

### BOJ11729: 하노이 탑 이동 순서

```python
def hanoi(a, b, n, depth=0):
    indent = '  ' * depth
    if n == 1:
        print(f"{indent}원판 1을 {a}번 기둥에서 {b}번 기둥으로 이동")
        return
    print(f"{indent}{n}개의 원판을 {a}번에서 {b}번으로 옮기기 시작 (보조: {6 - a - b})")
    hanoi(a, 6 - a - b, n - 1, depth + 1)
    print(f"{indent}원판 {n}을 {a}번 기둥에서 {b}번 기둥으로 이동")
    hanoi(6 - a - b, b, n - 1, depth + 1)
    print(f"{indent}{n}개의 원판을 {a}번에서 {b}번으로 옮기기 완료")

n = int(input("옮길 원판의 수를 입력하세요 : "))
print(f"총 이동 횟수 : {(1 << n) - 1}")
hanoi(1, 3, n)
```

```python
def hanoi(a, b, n):
    if n == 1:
        print(a, b)
        return
    hanoi(a, 6 - a - b, n - 1)
    print(a, b)
    hanoi(6 - a - b, b, n - 1)

n = int(input())
print((1 << n) - 1)
hanoi(1, 3, n)
```

```java
import java.util.Scanner;

public class Main {
    static StringBuilder sb = new StringBuilder();

    static void hanoi(int a, int b, int n) {
        if (n == 1) {
            sb.append(a).append(" ").append(b).append("\n");
            return;
        }
        
        hanoi(a, 6 - a - b, n - 1);
        sb.append(a).append(" ").append(b).append("\n");
        hanoi(6 - a - b, b, n - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        
        sb.append((1 << n) - 1).append("\n");
        hanoi(1, 3, n);
        System.out.print(sb);
    }
}
```

### BOJ1074: Z

```python
def func(n, r, c, depth=0):
    indent = '  ' * depth
    if n == 0:
        print(f"{indent}기저 도달 : n=0, (r={r}, c={c}) → 0")
        return 0
    num = 1 << (n - 1)
    size = num * num
    print(f"{indent}n={n}, (r={r}, c={c}), num={num}")
    if r < num and c < num:
        print(f"{indent}↳ 1사분면 : 좌상단")
        return func(n - 1, r, c, depth + 1)
    elif r < num and c >= num:
        print(f"{indent}↳ 2사분면 : 우상단, 누적 {size}")
        return size + func(n - 1, r, c - num, depth + 1)
    elif r >= num and c < num:
        print(f"{indent}↳ 3사분면 : 좌하단, 누적 {2 * size}")
        return 2 * size + func(n - 1, r - num, c, depth + 1)
    else:
        print(f"{indent}↳ 4사분면 : 우하단, 누적 {3 * size}")
        return 3 * size + func(n - 1, r - num, c - num, depth + 1)

N, r, c = map(int, input("N r c를 입력하세요 : ").split())
print(f"\nZ 순서 번호 : {func(N, r, c)}")
```

```python
def func(n, r, c):
    if n == 0:
        return 0
    half = 1 << (n - 1)
    if r < half and c < half:
        return func(n - 1, r, c)
    elif r < half and c >= half:
        return half * half + func(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * half * half + func(n - 1, r - half, c)
    else:
        return 3 * half * half + func(n - 1, r - half, c - half)

N, r, c = map(int, input().split())
print(func(N, r, c))
```

```java
import java.util.Scanner;

public class Main {
    static int func(int n, int r, int c) {
        if (n == 0) return 0;
        int half = 1 << (n - 1);

        if (r < half && c < half) return func(n - 1, r, c);
        else if (r < half && c >= half) return half * half + func(n - 1, r, c - half);
        else if (r >= half && c < half) return 2 * half * half + func(n - 1, r - half, c);
        else return 3 * half * half + func(n - 1, r - half, c - half);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int r = sc.nextInt();
        int c = sc.nextInt();
        
        System.out.println(func(n, r, c));
    }
}
```