import sys

lines = sys.stdin.read().splitlines()
for line in lines:
    l = sum(i.islower() for i in line)
    u = sum(i.isupper() for i in line)
    d = sum(i.isdigit() for i in line)
    s = sum(i.isspace() for i in line)
    print(l, u, d, s)