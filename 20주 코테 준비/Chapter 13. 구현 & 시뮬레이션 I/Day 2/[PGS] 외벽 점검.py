from itertools import permutations


def solution(n, weak, dist):
    l = len(weak)
    weak = weak + [w + n for w in weak]
    ans = len(dist) + 1
    for s in range(l):
        for i in permutations(dist):
            cnt = 1
            temp = weak[s] + i[cnt - 1]
            for idx in range(s, s + l):
                if weak[idx] > temp:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    temp = weak[idx] + i[cnt - 1]
            ans = min(ans, cnt)
    return ans if ans <= len(dist) else -1
