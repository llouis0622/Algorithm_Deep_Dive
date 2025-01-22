from collections import deque


def solution(bridge_length, weight, truck_weights):
    ans = 0
    num = 0
    sum_weights = 0
    q = deque()
    while True:
        if num == len(truck_weights):
            ans += bridge_length
            break
        ans += 1
        if len(q) == bridge_length:
            sum_weights -= q.popleft()
        tmp = truck_weights[num]
        if sum_weights + tmp <= weight:
            sum_weights += tmp
            q.append(tmp)
            num += 1
        else:
            q.append(0)
    return ans