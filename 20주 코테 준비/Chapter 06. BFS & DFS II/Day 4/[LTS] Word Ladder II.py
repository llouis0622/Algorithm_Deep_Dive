from collections import deque, defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        arr = set(wordList)
        if endWord not in arr:
            return []
        prev = defaultdict(list)
        dist = {beginWord: 0}
        q = deque([beginWord])
        found = False
        step = 0
        while q and not found:
            step += 1
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        nxt = word[:i] + j + word[i + 1:]
                        if nxt in arr:
                            if nxt not in dist:
                                dist[nxt] = step
                                q.append(nxt)
                                prev[nxt].append(word)
                            elif dist[nxt] == step:
                                prev[nxt].append(word)
                            if nxt == endWord:
                                found = True
            arr -= set(dist.keys())
        res = []

        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for i in prev[word]:
                dfs(i, path + [i])

        if endWord in dist:
            dfs(endWord, [endWord])
        return res
