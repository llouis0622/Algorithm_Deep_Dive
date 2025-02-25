import sys


def pair(n, heights):
    stack = []
    res = 0
    for h in heights:
        cnt = 1
        while stack and stack[-1][0] <= h:
            res += stack[-1][1]
            if stack[-1][0] == h:
                cnt += stack[-1][1]
            stack.pop()
        if stack:
            res += 1
        stack.append((h, cnt))
    return res


N = int(sys.stdin.readline())
heights = [int(sys.stdin.readline()) for _ in range(N)]
print(pair(N, heights))