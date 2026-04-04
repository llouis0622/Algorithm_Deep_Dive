import sys

input = sys.stdin.readline
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    arr = arr[1:]
    num = len(arr)
    stack = []
    ans = 0
    for i in range(num + 1):
        temp = arr[i] if i < num else 0
        while stack and arr[stack[-1]] >= temp:
            height = arr[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            ans = max(ans, height * width)
        stack.append(i)
    print(ans)
