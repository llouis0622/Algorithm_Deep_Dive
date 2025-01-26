import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()


def rectangle(H):
    stack = deque()
    tmp = 0
    H.append(0)
    for i, h in enumerate(H):
        while stack and H[stack[-1]] > h:
            height = H[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            tmp = max(tmp, height * width)
        stack.append(i)
    return tmp


for i in data:
    if i == "0":
        break
    value = list(map(int, i.split()))
    N, H = value[0], value[1:]
    print(rectangle(H))