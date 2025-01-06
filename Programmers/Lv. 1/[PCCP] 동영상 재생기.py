def time_to_sec(time):
    min, sec = map(int, time.split(':'))
    return min * 60 + sec


def sec_to_time(sec):
    min = sec // 60
    sec = sec % 60
    return f"{min:02}:{sec:02}"


def solution(video_len, pos, op_start, op_end, commands):
    video = time_to_sec(video_len)
    num = time_to_sec(pos)
    start = time_to_sec(op_start)
    end = time_to_sec(op_end)
    if start <= num <= end:
        num = end
    for i in commands:
        if i == "next":
            num = min(video, num + 10)
        elif i == "prev":
            num = max(0, num - 10)
        if start <= num <= end:
            num = end
    return sec_to_time(num)