class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        num = -1
        for i in range(N - 1, -1, -1):
            temp = arr[i]
            arr[i] = num
            if temp > num:
                num = temp
        return arr