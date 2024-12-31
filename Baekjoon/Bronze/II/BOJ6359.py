def escape(n):
    return int(n ** 0.5)


T = int(input())
res = []
for _ in range(T):
    n = int(input())
    res.append(escape(n))
print("\n".join(map(str, res)))