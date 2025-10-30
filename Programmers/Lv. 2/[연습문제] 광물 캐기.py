def solution(picks, minerals):
    n = min(len(minerals), (picks[0] + picks[1] + picks[2]) * 5)
    minerals = minerals[:n]
    res = []
    for i in range(0, len(minerals), 5):
        d = cnt = s = 0
        for m in minerals[i:i + 5]:
            if m == "diamond":
                d += 1
            elif m == "iron":
                cnt += 1
            else:
                s += 1
        num = 25 * d + 5 * cnt + s
        res.append((d, cnt, s, num))
    res.sort(key=lambda x: x[3], reverse=True)
    dia, iron, stone = picks
    temp = 0
    for d, cnt, s, _ in res:
        if dia > 0:
            dia -= 1
            temp += d + cnt + s
        elif iron > 0:
            iron -= 1
            temp += 5 * d + cnt + s
        elif stone > 0:
            stone -= 1
            temp += 25 * d + 5 * cnt + s
        else:
            break
    return temp