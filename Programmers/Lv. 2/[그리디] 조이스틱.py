def solution(name):
    ans = 0
    l = len(name)
    move = l - 1
    for i, char in enumerate(name):
        ans += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        idx = i + 1
        while idx < l and name[idx] == 'A':
            idx += 1
        move = min(move, i * 2 + l - idx, (l - idx) * 2 + i)
    return ans + move