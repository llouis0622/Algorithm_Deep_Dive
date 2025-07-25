def solution(bandage, health, attacks):
    t, x, y = bandage
    res = health
    combo = 0
    num = attacks[-1][0]
    temp = {a[0]: a[1] for a in attacks}
    for time in range(1, num + 1):
        if time in temp:
            health -= temp[time]
            if health <= 0:
                return -1
            combo = 0
        else:
            combo += 1
            health += x
            if combo == t:
                health += y
                combo = 0
            health = min(health, res)
    return health