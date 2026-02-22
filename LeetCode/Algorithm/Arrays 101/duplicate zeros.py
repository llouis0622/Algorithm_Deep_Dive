class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        z = arr.count(0)
        i = n - 1
        j = n + z - 1
        while i >= 0:
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            i -= 1
            j -= 1