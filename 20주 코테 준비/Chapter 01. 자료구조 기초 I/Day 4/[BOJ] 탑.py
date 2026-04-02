import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
ans = [0] * N
stack = []
for i in range(N - 1, -1, -1):
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = i + 1
    stack.append(i)
print(*ans)


# import sys
#
# input = sys.stdin.readline
# N = int(input())
# arr = list(map(int, input().split()))
# ans = [0] * N
# stack = []
# for i in range(N):
#     while stack and arr[stack[-1]] < arr[i]:
#         stack.pop()
#     if stack:
#         ans[i] = stack[-1] + 1
#     stack.append(i)
# print(*ans)
