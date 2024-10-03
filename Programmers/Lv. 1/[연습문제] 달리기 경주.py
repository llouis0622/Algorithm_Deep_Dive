def solution(players, callings):
    dict = {player: i for i, player in enumerate(players)}
    for i in callings:
        idx = dict[i]
        if idx > 0:
            temp = players[idx - 1]
            players[idx - 1], players[idx] = players[idx], players[idx - 1]
            dict[i] -= 1
            dict[temp] += 1
    return players