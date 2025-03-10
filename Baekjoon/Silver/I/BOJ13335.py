from collections import deque


def cross(n, w, L, trucks):
    bridge = deque([0] * w)
    time = 0
    cur = 0
    for t in trucks:
        while True:
            time += 1
            cur -= bridge.popleft()
            if cur + t <= L:
                bridge.append(t)
                cur += t
                break
            else:
                bridge.append(0)
    return time + w


n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
print(cross(n, w, L, trucks))