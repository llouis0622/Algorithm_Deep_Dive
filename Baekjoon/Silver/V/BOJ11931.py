import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
num = list(map(int, data[1:]))
num.sort(reverse=True)
print("\n".join(map(str, num)))