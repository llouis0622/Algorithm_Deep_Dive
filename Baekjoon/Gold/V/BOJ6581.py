import sys

s = sys.stdin.read().split()
out = sys.stdout
temp = 0
for i in s:
    if i == '<br>':
        out.write('\n')
        temp = 0
    elif i == '<hr>':
        if temp != 0:
            out.write('\n')
        out.write('-' * 80 + '\n')
        temp = 0
    else:
        L = len(i)
        if temp == 0:
            out.write(i)
            temp = L
        elif temp + 1 + L <= 80:
            out.write(' ')
            out.write(i)
            temp += 1 + L
        else:
            out.write('\n')
            out.write(i)
            temp = L
if temp != 0:
    out.write('\n')