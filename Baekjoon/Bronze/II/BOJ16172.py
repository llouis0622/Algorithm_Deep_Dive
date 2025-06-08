import sys

input = sys.stdin.read
S, K = input().split()
temp = ''.join(i for i in S if i.isalpha())
print(1 if K in temp else 0)