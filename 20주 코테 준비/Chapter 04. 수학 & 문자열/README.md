### 수학, 소수, 문자열

- GCD(최대공약수) : 유클리드 호제법 -> math.gcd(a, b)
- LCM(최소공배수) : a * b // gcd(a, b)
- 소수 판별 : O(sqrt n) 시도 나눗셈
- 에라토스테네스의 체 : n까지 모든 소수 O(n log log n)
- 문자열 : split, join, strip, replace 기본 + ord, chr 변환
- 대용량 문자열 결합 -> join 사용

```python
import math

math.gcd(a, b)
a * b // math.gcd(a, b)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sieve(n):
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_p[i]:
            for j in range(i * i, n + 1, i):
                is_p[j] = False
    return [i for i in range(2, n + 1) if is_p[i]]


s[::-1]  # 뒤집기
ord('A') - ord('a')  # 대소문자 변환
''.join(lst)  # 리스트 -> 문자열
```