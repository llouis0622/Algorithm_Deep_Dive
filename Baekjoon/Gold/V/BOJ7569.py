from collections import deque
import sys

input = sys.stdin.read
data = input().splitlines()

M, N, H = map(int, data[0].split())
box = []
queue = deque()
total = 0
dh = [-1, 1, 0, 0, 0, 0]
dn = [0, 0, -1, 1, 0, 0]
dm = [0, 0, 0, 0, -1, 1]
idx = 1
for h in range(H):
    lst = []
    for n in range(N):
        row = list(map(int, data[idx].split()))
        lst.append(row)
        for m in range(M):
            if row[m] == 1:
                queue.append((h, n, m))
            elif row[m] == 0:
                total += 1
        idx += 1
    box.append(lst)
num = 0
while queue and total > 0:
    for _ in range(len(queue)):
        h, n, m = queue.popleft()
        for i in range(6):
            nh, nn, nm = h + dh[i], n + dn[i], m + dm[i]
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and box[nh][nn][nm] == 0:
                box[nh][nn][nm] = 1
                queue.append((nh, nn, nm))
                total -= 1
    num += 1
if total > 0:
    print(-1)
else:
    print(num)