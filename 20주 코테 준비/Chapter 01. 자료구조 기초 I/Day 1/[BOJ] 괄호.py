import sys

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    stack = []
    check = True
    arr = input().strip()
    for i in arr:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                check = False
                break
    print('YES' if check and not stack else 'NO')


# import sys
#
# input = sys.stdin.readline
# N = int(input())
# for _ in range(N):
#     stack = []
#     for ch in input().strip():
#         if ch == '(':
#             stack.append(ch)
#         elif stack:
#             stack.pop()
#         else:
#             stack.append('X')
#             break
#     print('YES' if not stack else 'NO')
