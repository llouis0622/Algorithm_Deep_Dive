import sys

lines = sys.stdin.read().splitlines()
cnt = {}
for name in lines:
    cnt[name] = cnt.get(name, 0) + 1
num = len(lines)
for i in sorted(cnt):
    res = cnt[i] * 100 / num
    print(f"{i} {res:.4f}")