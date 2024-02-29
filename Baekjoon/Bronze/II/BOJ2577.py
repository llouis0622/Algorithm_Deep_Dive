import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
for i in range(10):
    print(list(str(A * B * C)).count(str(i)))