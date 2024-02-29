import sys

S = sys.stdin.readline()
for i in range(26):
    print(S.count(chr(ord('a') + i)), end=' ')