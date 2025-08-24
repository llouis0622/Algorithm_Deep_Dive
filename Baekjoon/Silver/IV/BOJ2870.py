import sys, re

input = sys.stdin.readline
n = int(input().strip())
num = []
for _ in range(n):
    temp = input().strip()
    for i in re.findall(r'\d+', temp):
        i = i.lstrip('0')
        if i == '':
            i = '0'
        num.append(int(i))
num.sort()
print('\n'.join(str(i) for i in num))