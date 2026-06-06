class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        temp = {}
        for i, char in enumerate(s):
            temp[char] = i
        ans = []
        start = end = 0
        for i, char in enumerate(s):
            end = max(end, temp[char])
            if i == end:
                ans.append(end - start + 1)
                start = i + 1
        return ans
