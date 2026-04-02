import sys

input = sys.stdin.readline
N = int(input())
arr = input().strip()
num = [int(input()) for _ in range(N)]
stack = []
for i in arr:
    if 'A' <= i <= 'Z':
        stack.append(num[ord(i) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        if i == "+":
            stack.append(a + b)
        elif i == "-":
            stack.append(a - b)
        elif i == "*":
            stack.append(a * b)
        else:
            stack.append(a / b)
print(f'{stack[0]:.2f}')
