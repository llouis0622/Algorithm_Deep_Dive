import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])


def reverse(num):
    return int(num[::-1])


temp = [reverse(data[i + 1]) for i in range(N)]
temp.sort()
print("\n".join(map(str, temp)))