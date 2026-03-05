class Solution:
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        m = len(nums) // 2
        l = nums[:m]
        r = nums[m:]
        l = self.sortArray(l)
        r = self.sortArray(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                nums[k] = l[i]
                i += 1
            else:
                nums[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            nums[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            nums[k] = r[j]
            j += 1
            k += 1
        return nums