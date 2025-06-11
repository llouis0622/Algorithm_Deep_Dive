N = int(input())
s = "SciComLove"
N %= len(s)
print(s[N:] + s[:N])