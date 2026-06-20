from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    def check(a, b):
        cnt = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt += 1
        return cnt == 1

    q = deque()
    q.append((begin, 0))
    visited = [False] * len(words)
    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            if not visited[i] and check(word, words[i]):
                visited[i] = True
                q.append((words[i], cnt + 1))
    return 0
