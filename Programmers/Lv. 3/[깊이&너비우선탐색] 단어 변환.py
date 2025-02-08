from collections import deque


def check(word1, word2):
    return sum(a != b for a, b in zip(word1, word2)) == 1


def solution(begin, target, words):
    if target not in words:
        return 0
    queue = deque([(begin, 0)])
    visited = set()
    while queue:
        cur, temp = queue.popleft()
        if cur == target:
            return temp
        for word in words:
            if word not in visited and check(cur, word):
                visited.add(word)
                queue.append((word, temp + 1))
    return 0