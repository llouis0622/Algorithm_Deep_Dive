import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
num = list(map(int, data[1:]))
num.sort()
print("\n".join(map(str, num)))