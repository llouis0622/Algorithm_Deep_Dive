import sys

input = sys.stdin.readline
t = int(input().strip())
for _ in range(t):
    temp = input().strip().split()
    ans = set()
    while True:
        s = input().strip()
        if s == "what does the fox say?":
            break
        ans.add(s.rsplit(' ', 1)[-1])
    print(' '.join(i for i in temp if i not in ans))