import sys, heapq

input = sys.stdin.readline

N = int(input().strip())
min_heap, max_heap = [], []
temp = {}
for _ in range(N):
    P, L = map(int, input().split())
    temp[P] = L
    heapq.heappush(min_heap, (L, P))
    heapq.heappush(max_heap, (-L, -P))
M = int(input().strip())
ans = []
for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'recommend':
        x = int(cmd[1])
        if x == 1:
            while max_heap:
                L_num, P_num = max_heap[0]
                P = -P_num
                L = -L_num
                if P in temp and temp[P] == L:
                    ans.append(str(P))
                    break
                heapq.heappop(max_heap)
        else:
            while min_heap:
                L, P = min_heap[0]
                if P in temp and temp[P] == L:
                    ans.append(str(P))
                    break
                heapq.heappop(min_heap)
    elif cmd[0] == 'add':
        P = int(cmd[1])
        L = int(cmd[2])
        temp[P] = L
        heapq.heappush(min_heap, (L, P))
        heapq.heappush(max_heap, (-L, -P))
    elif cmd[0] == 'solved':
        P = int(cmd[1])
        if P in temp:
            temp.pop(P, None)
print("\n".join(ans))