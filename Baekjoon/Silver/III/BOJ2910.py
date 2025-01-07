from collections import Counter
import sys

input = sys.stdin.read
data = input().split()

N, C = map(int, data[:2])
temp = list(map(int, data[2:]))
cnt = Counter(temp)
num = sorted(temp, key=lambda x: (-cnt[x], temp.index(x)))
print(" ".join(map(str, num)))