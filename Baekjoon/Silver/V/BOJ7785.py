import sys

input = sys.stdin.readline

n = int(input())
office = set()
for _ in range(n):
    name, status = input().split()
    if status == "enter":
        office.add(name)
    else:
        office.remove(name)
for name in sorted(office, reverse=True):
    print(name)