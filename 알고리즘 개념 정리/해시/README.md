## 1️⃣ 해시

- 키를 값에 매핑할 수 있는 구조로서 연관 배열 추가에 사용되는 자료구조
- 파이썬의 딕셔너리와 동일

### 해시 함수

- 임의 길이의 데이터를 고정된 길이의 데이터로 대응시키는 함수

### 충돌 회피 방식 - Chaining

- 충돌 발생 시 각 해시 버킷에 리스트를 두어, 같은 해시 값을 가진 데이터를 그 리스트에 이어서 저장하는 방식
- 장점 : 동적 크기 조절 가능
- 단점 : 공간 비효율, 캐시 효율 저하

### 충돌 회피 방식 - Open Addressing(Linear Probing)

- 충돌 발생 시 오른쪽으로 1칸씩 이동하는 방식
- 장점 : Cache Hit Rate가 높음
- 단점 : Clustering이 생겨 성능에 영향을 줄 수 있음

### 충돌 회피 방식 - Open Addressing(Quadratic Probing)

- 충돌 발생 시 오른쪽으로 1, 3, 5, ... 칸씩 이동하는 방식
- 장점 : Cache Hit Rate가 나쁘지 않음, Clustering을 어느 정도 회피할 수 있음
- 단점 : 해시 값이 같을 경우 여전히 Clustering이 발생함

### 충돌 회피 방식 - Open Addressing(Double Probing)

- 충돌 발생 시 오른쪽으로 이동할 칸의 수를 새로운 해시 함수로 계산하는 방식
- 장점 : Clustering을 효과적으로 회피할 수 있음
- 단점 : Cache Hit Rate가 낮음

## 2️⃣ 해시 풀이 방법

### **해시 선택 가능성**

- 탐색을 매우 빠르게 하고 싶을 때
- 중복 여부를 빠르게 판단할 때(방문 체크, 중복 제거)
- 빈도나 개수를 세야 할 때
- 쌍을 찾아야 할 때

### **해시 문제 판별법**

- 이 수가 존재하는지 판단하라 → 탐색 O(1), 해시
- 중복을 제거하라 → set or dict
- 빈도를 계산하라 → dict or Counter
- 두 수의 합이 x인 쌍이 있는지 찾기 → 보조 집합 활용
- 빠르게 포함 여부를 판별해야 함 → 정렬보다 해시

### **해시 풀이 기본 흐름**

- 적절한 자료구조 선택 - 중복 제거 set(), 키-값 저장 dict(), 빈도 세기 Counter
- 값 저장 or 카운팅
- 포함 여부 및 빈도 확인
- 조건에 따라 카운트, 출력, 조합 구성 등

## 3️⃣ 수업 코드

### BOJ7785: 회사에 있는 사람

```python
n = int(input())
office = set()
for _ in range(n):
    name, status = input().split()
    if status == "enter":
        office.add(name)
    else:
        office.remove(name)
for name in sorted(office, reverse=True):
    print(name)
```

```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashSet<String> set = new HashSet<>();

        for (int i = 0; i < n; i++) {
            String[] parts = br.readLine().split(" ");
            String name = parts[0];
            String log = parts[1];
            if (log.equals("enter")) {
                set.add(name);
            } else {
                set.remove(name);
            }
        }

        List<String> result = new ArrayList<>(set);
        result.sort(Comparator.reverseOrder());

        for (String name : result) {
            System.out.println(name);
        }
    }
}
```

### BOJ1620: 나는야 포켓몬 마스터 이다솜

```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num2name = ['']
name2num = {}
for i in range(1, n + 1):
    name = input().strip()
    num2name.append(name)
    name2num[name] = i
for _ in range(m):
    q = input().strip()
    if q.isdigit():
        print(num2name[int(q)])
    else:
        print(name2num[q])
```

```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        String[] numToName = new String[n + 1];
        HashMap<String, Integer> nameToNum = new HashMap<>();

        for (int i = 1; i <= n; i++) {
            String name = br.readLine().trim();
            numToName[i] = name;
            nameToNum.put(name, i);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            String q = br.readLine().trim();
            if (Character.isDigit(q.charAt(0))) {
                sb.append(numToName[Integer.parseInt(q)]).append('\n');
            } else {
                sb.append(nameToNum.get(q)).append('\n');
            }
        }

        System.out.print(sb);
    }
}
```

### Chaining 해시 구현

```python
M = 1_000_003
a = 1000
MX = 500_005

head = [-1] * M
pre = [-1] * MX
nxt = [-1] * MX
key = [''] * MX
val = [0] * MX
unused = 0

def my_hash(s):
    h = 0
    for x in s:
        h = (h * a + ord(x)) % M
    return h

def find(k):
    # 문자열 k에 대해 해시값 h를 구한다
    # head[h]를 통해 체인의 첫 번째 인덱스를 얻는다
    # 연결리스트처럼 idx를 따라가며 key[idx]가 k와 일치하는지 확인한다
    # 일치하면 해당 인덱스를 리턴
    # 끝까지 없으면 -1을 리턴
    pass

def insert(k, v):
    # find(k)로 이미 존재하는 키인지 확인한다
    # 존재한다면 val[idx]를 새 값으로 갱신하고 종료
    # 존재하지 않으면 새로운 unused 인덱스에 key와 val을 저장
    # head[h]가 -1이 아니라면 연결리스트 앞에 삽입하므로,
    # nxt[unused] = head[h], pre[head[h]] = unused 처리를 한다
    # head[h]를 unused로 업데이트한다
    # unused 값을 1 증가시킨다
    pass

def erase(k):
    # find(k)를 통해 삭제할 인덱스를 찾는다
    # 찾지 못하면 아무것도 하지 않고 종료
    # 연결리스트 내에서 해당 노드를 제거:
    # pre[idx]가 있다면 nxt[pre[idx]] = nxt[idx]
    # nxt[idx]가 있다면 pre[nxt[idx]] = pre[idx]
    # head[h]가 idx라면 head[h] = nxt[idx]로 갱신
    pass

def test():
    insert("orange", 724)
    insert("melon", 20)
    assert val[find("melon")] == 20
    insert("banana", 52)
    insert("cherry", 27)
    insert("orange", 100)
    assert val[find("banana")] == 52
    assert val[find("orange")] == 100
    erase("wrong_fruit")
    erase("orange")
    assert find("orange") == -1
    erase("orange")
    insert("orange", 15)
    assert val[find("orange")] == 15
    insert("apple", 36)
    insert("lemon", 6)
    insert("orange", 701)
    assert val[find("cherry")] == 27
    erase("xxxxxxx")
    assert find("xxxxxxx") == -1
    assert val[find("apple")] == 36
    assert val[find("melon")] == 20
    assert val[find("banana")] == 52
    assert val[find("cherry")] == 27
    assert val[find("orange")] == 701
    assert val[find("lemon")] == 6
    print("good!")

test()
```

```java
import java.util.*;

public class MyHashTable {
    static final int M = 1000003;
    static final int a = 1000;
    static final int MX = 500005;

    static int[] head = new int[M];
    static int[] pre = new int[MX];
    static int[] nxt = new int[MX];
    static String[] key = new String[MX];
    static int[] val = new int[MX];
    static int unused = 0;

    public static void main(String[] args) {
        Arrays.fill(head, -1);
        Arrays.fill(pre, -1);
        Arrays.fill(nxt, -1);
        test();
    }

    static int myHash(String s) {
        int h = 0;
        for (int i = 0; i < s.length(); i++) {
            h = (int) (((long) h * a + s.charAt(i)) % M);
        }
        return h;
    }

    static int find(String k) {
        // 1. k에 대해 해시값 h를 계산
        // 2. head[h]부터 시작해 체인을 순회
        // 3. key[idx]가 k와 같다면 그 idx를 반환
        // 4. 끝까지 못 찾으면 -1 반환
        return -1;
    }

    static void insert(String k, int v) {
        // 1. find(k)로 기존에 존재하는지 확인
        // 2. 존재하면 해당 idx에 대해 val[idx] = v로 갱신
        // 3. 존재하지 않으면 unused 위치에 key와 val 저장
        // 4. nxt[unused] = head[h] 처리
        // 5. pre[head[h]] = unused 처리 (단 head[h] != -1일 때)
        // 6. head[h] = unused로 갱신
        // 7. unused 증가
    }

    static void erase(String k) {
        // 1. find(k)로 idx 탐색
        // 2. 없으면 아무 일도 하지 않음
        // 3. 연결 리스트에서 제거 작업
        // 4. head[h] == idx일 경우 head[h] = nxt[idx]
    }

    static void test() {
        insert("orange", 724);
        insert("melon", 20);
        assert val[find("melon")] == 20;
        insert("banana", 52);
        insert("cherry", 27);
        insert("orange", 100);
        assert val[find("banana")] == 52;
        assert val[find("orange")] == 100;
        erase("wrong_fruit");
        erase("orange");
        assert find("orange") == -1;
        erase("orange");
        insert("orange", 15);
        assert val[find("orange")] == 15;
        insert("apple", 36);
        insert("lemon", 6);
        insert("orange", 701);
        assert val[find("cherry")] == 27;
        erase("xxxxxxx");
        assert find("xxxxxxx") == -1;
        assert val[find("apple")] == 36;
        assert val[find("melon")] == 20;
        assert val[find("banana")] == 52;
        assert val[find("cherry")] == 27;
        assert val[find("orange")] == 701;
        assert val[find("lemon")] == 6;
        System.out.println("good!");
    }
}
```

### Chaining 해시 구현 정답

```python
M = 1_000_003
a = 1000
MX = 500_005

head = [-1] * M
pre = [-1] * MX
nxt = [-1] * MX
key = [''] * MX
val = [0] * MX
unused = 0

def my_hash(s):
    h = 0
    for x in s:
        h = (h * a + ord(x)) % M
    return h

# key[idx] == k인 idx를 반환, 없으면 -1
def find(k):
    h = my_hash(k)
    idx = head[h]
    while idx != -1:
        if key[idx] == k:
            return idx
        idx = nxt[idx]
    return -1

def insert(k, v):
    global unused
    idx = find(k)
    if idx != -1:
        val[idx] = v
        return
    h = my_hash(k)
    key[unused] = k
    val[unused] = v
    if head[h] != -1:
        nxt[unused] = head[h]
        pre[head[h]] = unused
    head[h] = unused
    unused += 1

def erase(k):
    idx = find(k)
    if idx == -1:
        return
    if pre[idx] != -1:
        nxt[pre[idx]] = nxt[idx]
    if nxt[idx] != -1:
        pre[nxt[idx]] = pre[idx]
    h = my_hash(k)
    if head[h] == idx:
        head[h] = nxt[idx]

def test():
    insert("orange", 724)
    insert("melon", 20)
    assert val[find("melon")] == 20
    insert("banana", 52)
    insert("cherry", 27)
    insert("orange", 100)
    assert val[find("banana")] == 52
    assert val[find("orange")] == 100
    erase("wrong_fruit")
    erase("orange")
    assert find("orange") == -1
    erase("orange")
    insert("orange", 15)
    assert val[find("orange")] == 15
    insert("apple", 36)
    insert("lemon", 6)
    insert("orange", 701)
    assert val[find("cherry")] == 27
    erase("xxxxxxx")
    assert find("xxxxxxx") == -1
    assert val[find("apple")] == 36
    assert val[find("melon")] == 20
    assert val[find("banana")] == 52
    assert val[find("cherry")] == 27
    assert val[find("orange")] == 701
    assert val[find("lemon")] == 6
    print("good!")

test()
```

```java
import java.util.*;

public class MyHashTable {
    static final int M = 1000003;
    static final int a = 1000;
    static final int MX = 500005;

    static int[] head = new int[M];
    static int[] pre = new int[MX];
    static int[] nxt = new int[MX];
    static String[] key = new String[MX];
    static int[] val = new int[MX];
    static int unused = 0;

    public static void main(String[] args) {
        Arrays.fill(head, -1);
        Arrays.fill(pre, -1);
        Arrays.fill(nxt, -1);
        test();
    }

    static int myHash(String s) {
        int h = 0;
        for (int i = 0; i < s.length(); i++) {
            h = (int) (((long) h * a + s.charAt(i)) % M);
        }
        return h;
    }

    static int find(String k) {
        int h = myHash(k);
        int idx = head[h];
        while (idx != -1) {
            if (key[idx].equals(k)) return idx;
            idx = nxt[idx];
        }
        return -1;
    }

    static void insert(String k, int v) {
        int idx = find(k);
        if (idx != -1) {
            val[idx] = v;
            return;
        }
        int h = myHash(k);
        key[unused] = k;
        val[unused] = v;
        nxt[unused] = head[h];
        if (head[h] != -1) {
            pre[head[h]] = unused;
        }
        head[h] = unused;
        unused++;
    }

    static void erase(String k) {
        int idx = find(k);
        if (idx == -1) return;
        if (pre[idx] != -1) nxt[pre[idx]] = nxt[idx];
        if (nxt[idx] != -1) pre[nxt[idx]] = pre[idx];
        int h = myHash(k);
        if (head[h] == idx) head[h] = nxt[idx];
    }

    static void test() {
        insert("orange", 724);
        insert("melon", 20);
        assert val[find("melon")] == 20;
        insert("banana", 52);
        insert("cherry", 27);
        insert("orange", 100);
        assert val[find("banana")] == 52;
        assert val[find("orange")] == 100;
        erase("wrong_fruit");
        erase("orange");
        assert find("orange") == -1;
        erase("orange");
        insert("orange", 15);
        assert val[find("orange")] == 15;
        insert("apple", 36);
        insert("lemon", 6);
        insert("orange", 701);
        assert val[find("cherry")] == 27;
        erase("xxxxxxx");
        assert find("xxxxxxx") == -1;
        assert val[find("apple")] == 36;
        assert val[find("melon")] == 20;
        assert val[find("banana")] == 52;
        assert val[find("cherry")] == 27;
        assert val[find("orange")] == 701;
        assert val[find("lemon")] == 6;
        System.out.println("good!");
    }
}
```

### Open Addressing 해시 구현

```python
M = 1000003
a = 1000
EMPTY = -1
OCCUPY = 0
DUMMY = 1

status = [EMPTY] * M
key = [None] * M
val = [0] * M

def my_hash(s):
    h = 0
    for ch in s:
        h = (h * a + ord(ch)) % M
    return h

def find(k):
    # 1. k의 해시값 h를 계산한다.
    # 2. h부터 시작해 순차적으로 탐색 (선형 탐사)
    # 3. status[h] == EMPTY면 탐색 종료 (-1 반환)
    # 4. status[h] == OCCUPY이고 key[h] == k이면 h 반환
    # 5. 아니라면 (DUMMY거나 다른 키면) h = (h + 1) % M 하고 반복
    # 6. 끝까지 못 찾으면 -1 반환
    pass

def insert(k, v):
    # 1. find(k) 호출 → 이미 존재한다면 해당 위치 val[h] = v 갱신 후 종료
    # 2. 존재하지 않는다면 h = my_hash(k)부터 선형 탐사
    # 3. status[h]가 OCCUPY가 아닌 (EMPTY or DUMMY) 위치 찾기
    # 4. key[h] = k, val[h] = v, status[h] = OCCUPY 저장
    pass

def erase(k):
    # 1. find(k) 호출해서 idx 찾기
    # 2. idx == -1이면 아무것도 안함
    # 3. 존재하면 status[idx] = DUMMY로 마킹 (실제 삭제는 아님)
    pass

def test():
    insert("orange", 724)
    insert("melon", 20)
    assert val[find("melon")] == 20
    insert("banana", 52)
    insert("cherry", 27)
    insert("orange", 100)
    assert val[find("banana")] == 52
    assert val[find("orange")] == 100
    erase("wrong_fruit")
    erase("orange")
    assert find("orange") == -1
    erase("orange")
    insert("orange", 15)
    assert val[find("orange")] == 15
    insert("apple", 36)
    insert("lemon", 6)
    insert("orange", 701)
    assert val[find("cherry")] == 27
    erase("xxxxxxx")
    assert find("xxxxxxx") == -1
    assert val[find("apple")] == 36
    assert val[find("melon")] == 20
    assert val[find("banana")] == 52
    assert val[find("cherry")] == 27
    assert val[find("orange")] == 701
    assert val[find("lemon")] == 6
    print("good!")

test()
```

```java
import java.util.*;

public class MyOpenHash {
    static final int M = 1000003;
    static final int a = 1000;
    static final int EMPTY = -1;
    static final int OCCUPY = 0;
    static final int DUMMY = 1;

    static int[] status = new int[M];
    static String[] key = new String[M];
    static int[] val = new int[M];

    public static void main(String[] args) {
        Arrays.fill(status, EMPTY);
        test();
    }

    static int myHash(String s) {
        int h = 0;
        for (int i = 0; i < s.length(); i++)
            h = (int) (((long) h * a + s.charAt(i)) % M);
        return h;
    }

    static int find(String k) {
        // 1. k에 대한 해시값 h를 계산
        // 2. h부터 선형 탐사 시작
        // 3. status[h] == EMPTY면 -1 반환 (없음)
        // 4. status[h] == OCCUPY && key[h] == k이면 h 반환
        // 5. 아니면 h = (h + 1) % M 하고 반복
        // 6. 못 찾으면 -1 반환
        return -1;
    }

    static void insert(String k, int v) {
        // 1. find(k)로 존재 확인
        // 2. 존재하면 val[h] = v 로 갱신하고 종료
        // 3. 존재하지 않으면 h부터 OCCUPY 아닌 곳(EMPTY, DUMMY) 탐색
        // 4. key[h] = k, val[h] = v, status[h] = OCCUPY 저장
    }

    static void erase(String k) {
        // 1. find(k)로 h 위치 확인
        // 2. 없으면 아무것도 안함
        // 3. 있으면 status[h] = DUMMY 마킹
    }

    static void test() {
        insert("orange", 724);
        insert("melon", 20);
        assert val[find("melon")] == 20;
        insert("banana", 52);
        insert("cherry", 27);
        insert("orange", 100);
        assert val[find("banana")] == 52;
        assert val[find("orange")] == 100;
        erase("wrong_fruit");
        erase("orange");
        assert find("orange") == -1;
        erase("orange");
        insert("orange", 15);
        assert val[find("orange")] == 15;
        insert("apple", 36);
        insert("lemon", 6);
        insert("orange", 701);
        assert val[find("cherry")] == 27;
        erase("xxxxxxx");
        assert find("xxxxxxx") == -1;
        assert val[find("apple")] == 36;
        assert val[find("melon")] == 20;
        assert val[find("banana")] == 52;
        assert val[find("cherry")] == 27;
        assert val[find("orange")] == 701;
        assert val[find("lemon")] == 6;
        System.out.println("good!");
    }
}
```

### Open Addressing 해시 구현 정답

```python
M = 1000003
a = 1000
EMPTY = -1
OCCUPY = 0
DUMMY = 1

status = [EMPTY] * M
key = [None] * M
val = [0] * M

def my_hash(s):
    h = 0
    for ch in s:
        h = (h * a + ord(ch)) % M
    return h

def find(k):
    h = my_hash(k)
    start = h
    while status[h] != EMPTY:
        if status[h] == OCCUPY and key[h] == k:
            return h
        h = (h + 1) % M
        if h == start:
            break
    return -1

def insert(k, v):
    idx = find(k)
    if idx != -1:
        val[idx] = v
        return
    h = my_hash(k)
    while status[h] == OCCUPY:
        h = (h + 1) % M
    key[h] = k
    val[h] = v
    status[h] = OCCUPY

def erase(k):
    idx = find(k)
    if idx != -1:
        status[idx] = DUMMY

def test():
    insert("orange", 724)
    insert("melon", 20)
    assert val[find("melon")] == 20
    insert("banana", 52)
    insert("cherry", 27)
    insert("orange", 100)
    assert val[find("banana")] == 52
    assert val[find("orange")] == 100
    erase("wrong_fruit")
    erase("orange")
    assert find("orange") == -1
    erase("orange")
    insert("orange", 15)
    assert val[find("orange")] == 15
    insert("apple", 36)
    insert("lemon", 6)
    insert("orange", 701)
    assert val[find("cherry")] == 27
    erase("xxxxxxx")
    assert find("xxxxxxx") == -1
    assert val[find("apple")] == 36
    assert val[find("melon")] == 20
    assert val[find("banana")] == 52
    assert val[find("cherry")] == 27
    assert val[find("orange")] == 701
    assert val[find("lemon")] == 6
    print("good!")

test()
```

```java
import java.util.*;

public class MyOpenHash {
    static final int M = 1000003;
    static final int a = 1000;
    static final int EMPTY = -1;
    static final int OCCUPY = 0;
    static final int DUMMY = 1;

    static int[] status = new int[M];
    static String[] key = new String[M];
    static int[] val = new int[M];

    static int myHash(String s) {
        int h = 0;
        for (char ch : s.toCharArray())
            h = (int) (((long) h * a + ch) % M);
        return h;
    }

    static int find(String k) {
        int h = myHash(k);
        int start = h;
        while (status[h] != EMPTY) {
            if (status[h] == OCCUPY && key[h].equals(k)) return h;
            h = (h + 1) % M;
            if (h == start) break;
        }
        return -1;
    }

    static void insert(String k, int v) {
        int idx = find(k);
        if (idx != -1) {
            val[idx] = v;
            return;
        }
        int h = myHash(k);
        while (status[h] == OCCUPY) h = (h + 1) % M;
        key[h] = k;
        val[h] = v;
        status[h] = OCCUPY;
    }

    static void erase(String k) {
        int idx = find(k);
        if (idx != -1) status[idx] = DUMMY;
    }

    static void test() {
        Arrays.fill(status, EMPTY);

        insert("orange", 724);
        insert("melon", 20);
        assert val[find("melon")] == 20;
        insert("banana", 52);
        insert("cherry", 27);
        insert("orange", 100);
        assert val[find("banana")] == 52;
        assert val[find("orange")] == 100;
        erase("wrong_fruit");
        erase("orange");
        assert find("orange") == -1;
        erase("orange");
        insert("orange", 15);
        assert val[find("orange")] == 15;
        insert("apple", 36);
        insert("lemon", 6);
        insert("orange", 701);
        assert val[find("cherry")] == 27;
        erase("xxxxxxx");
        assert find("xxxxxxx") == -1;
        assert val[find("apple")] == 36;
        assert val[find("melon")] == 20;
        assert val[find("banana")] == 52;
        assert val[find("cherry")] == 27;
        assert val[find("orange")] == 701;
        assert val[find("lemon")] == 6;

        System.out.println("good!");
    }

    public static void main(String[] args) {
        test();
    }
}
```