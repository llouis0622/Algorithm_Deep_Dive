import sys

input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    name, kor, eng, math = input().split()
    arr.append([name, int(kor), int(eng), int(math)])
arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in arr:
    print(i[0])
