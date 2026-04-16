import math
from itertools import permutations


def solution(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


    arr = set()
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            num = int(''.join(j))
            arr.add(num)
    cnt = sum(1 for i in arr if is_prime(i))
    return cnt
