import sys

lines = sys.stdin.read().splitlines()
for line in lines:
    res = ''
    for i in range(0, len(line), 2):
        temp = line[i:i + 2]
        char = chr(int(temp, 16))
        res += char
    print(res)