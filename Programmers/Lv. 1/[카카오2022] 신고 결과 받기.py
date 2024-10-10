def solution(id_list, report, k):
    report = set(report)
    cnt = {user: 0 for user in id_list}
    alert = {user: [] for user in id_list}
    for i in report:
        id, id2report = i.split()
        alert[id].append(id2report)
        cnt[id2report] += 1
    stop = {user for user, count in cnt.items() if count >= k}
    res = [0] * len(id_list)
    for idx, user in enumerate(id_list):
        res[idx] = sum(1 for reported_user in alert[user] if reported_user in stop)
    return res