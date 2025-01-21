N = int(input())
cnt = 0
for _ in range(N):
    word = input().strip()
    stack = []
    for i in word:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        cnt += 1
print(cnt)