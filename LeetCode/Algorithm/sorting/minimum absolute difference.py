class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        num = 10 ** 18
        for i in range(1, len(arr)):
            d = arr[i] - arr[i - 1]
            if d < num:
                num = d
        res = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == num:
                res.append([arr[i - 1], arr[i]])
        return res