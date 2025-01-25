N = int(input())
H = list(map(int, input().split()))
stack = []
res = [0] * N
for i in range(N):
    while stack and H[stack[-1]] < H[i]:
        stack.pop()
    res[i] = stack[-1] + 1 if stack else 0
    stack.append(i)
print(' '.join(map(str, res)))