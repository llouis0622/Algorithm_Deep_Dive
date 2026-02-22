class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        S = set()
        for i in arr:
            if 2 * i in S or (i % 2 == 0 and i // 2 in S):
                return True
            S.add(i)
        return False