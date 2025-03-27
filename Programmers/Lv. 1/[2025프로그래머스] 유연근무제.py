def solution(schedules, timelogs, startday):
    ans = 0
    week = [(startday - 1 + i) % 7 for i in range(7)]
    for i in range(len(schedules)):
        temp = schedules[i]
        hour = temp // 100
        minute = temp % 100 + 10
        if minute >= 60:
            hour += 1
            minute -= 60
        num = hour * 100 + minute
        check = True
        for j in range(7):
            if week[j] >= 5:
                continue
            if timelogs[i][j] > num:
                check = False
                break
        if check:
            ans += 1
    return ans