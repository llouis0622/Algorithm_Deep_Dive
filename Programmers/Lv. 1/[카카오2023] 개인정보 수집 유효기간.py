def solution(today, terms, privacies):
    def date_to_days(date):
        y, m, d = map(int, date.split('.'))
        return y * 12 * 28 + m * 28 + d

    day = date_to_days(today)
    dict = {}
    for i in terms:
        type, num = i.split()
        dict[type] = int(num)
    res = []
    for i, j in enumerate(privacies):
        privacy, type = j.split()
        cnt_day = date_to_days(privacy)
        temp_day = cnt_day + dict[type] * 28 - 1
        if temp_day < day:
            res.append(i + 1)
    return res