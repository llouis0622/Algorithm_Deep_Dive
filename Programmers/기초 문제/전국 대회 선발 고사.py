def solution(rank, attendance):
    lst = [(rank[i], i) for i in range(len(rank)) if attendance[i]]
    lst.sort()
    ans = [i[1] for i in lst[:3]]
    return 10000 * ans[0] + 100 * ans[1] + ans[2]