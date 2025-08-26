import sys

s = sys.stdin.readline().strip()
if '::' in s:
    l, r = s.split('::', 1)
    left = l.split(':') if l else []
    right = r.split(':') if r else []
    temp = 8 - (len(left) + len(right))
    arr = left + (['0'] * temp) + right
else:
    arr = s.split(':')
arr = [i.zfill(4) for i in arr]
print(':'.join(arr))