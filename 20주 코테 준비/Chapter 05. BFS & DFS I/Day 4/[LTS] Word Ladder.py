from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        q = deque()
        q.append((beginWord, 1))
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    temp = word[:i] + j + word[i + 1:]
                    if temp in words:
                        words.remove(temp)
                        q.append((temp, length + 1))
        return 0
