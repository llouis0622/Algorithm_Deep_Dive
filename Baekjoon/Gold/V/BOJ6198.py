N = int(input())
H = [int(input()) for _ in range(N)]
stack = []
res = 0
for i in range(N):
    while stack and stack[-1] <= H[i]:
        stack.pop()
    res += len(stack)
    stack.append(H[i])
print(res)