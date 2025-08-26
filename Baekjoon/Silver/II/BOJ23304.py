import sys

s = sys.stdin.readline().strip()


def check(a, b):
    while a < b:
        if s[a] != s[b]:
            return False
        a += 1
        b -= 1
    return True


def akaraka(a, b):
    if a >= b:
        return True
    if not check(a, b):
        return False
    m = (b - a + 1) // 2
    return akaraka(a, a + m - 1)


print("AKARAKA" if akaraka(0, len(s) - 1) else "IPSELENTI")