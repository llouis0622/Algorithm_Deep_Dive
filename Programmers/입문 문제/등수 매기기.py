def solution(score):
    avg = [(i[0] + i[1]) / 2 for i in score]
    lst = sorted(avg, reverse=True)
    ans = [lst.index(i) + 1 for i in avg]
    return ans