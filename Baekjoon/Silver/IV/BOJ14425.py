from sys import stdin

input = stdin.readline


class Node(object):
    def __init__(self, isEnd):
        self.isEnd = isEnd
        self.childNode = {}


class Trie(object):
    def __init__(self):
        self.parent = Node(None)

    def insert(self, string):
        nowNode = self.parent
        temp_lenght = 0

        for char in string:
            if char not in nowNode.childNode:
                nowNode.childNode[char] = Node(char)

            nowNode = nowNode.childNode[char]
            temp_lenght += 1

            if temp_lenght == len(string):
                nowNode.isEnd = True

    def search(self, string):
        nowNode = self.parent
        temp_lenght = 0

        for char in string:
            if char in nowNode.childNode:
                nowNode = nowNode.childNode[char]
                temp_lenght += 1

                if temp_lenght == len(string) and nowNode.isEnd == True:
                    return True
            else:
                return False

        return False


N, M = map(int, input().split())
myTrie = Trie()

for _ in range(N):
    word = input().strip()
    myTrie.insert(word)

result = 0

for _ in range(M):
    word = input().strip()

    if myTrie.search(word):
        result += 1

print(result)


# import sys

# input = sys.stdin.readline
# n, m = map(int, input().split())
# textList = set([input() for _ in range(n)])
# count = 0

# for _ in range(m):
#     subText = input()

#     if subText in textList:
#         count += 1

# print(count)