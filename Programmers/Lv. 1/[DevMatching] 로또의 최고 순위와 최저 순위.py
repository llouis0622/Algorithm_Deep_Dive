def solution(lottos, win_nums):
    cnt = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)
    best = cnt + zero
    worst = cnt

    best_rank = 7 - best if best >= 2 else 6
    worst_rank = 7 - worst if worst >= 2 else 6

    return [best_rank, worst_rank]