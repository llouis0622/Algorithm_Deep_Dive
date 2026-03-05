import random


class Solution:
    def findKthLargest(self, nums, k):
        res = len(nums) - k
        l = 0
        r = len(nums) - 1
        while l <= r:
            p = random.randint(l, r)
            nums[p], nums[r] = nums[r], nums[p]
            c = nums[r]
            i = l
            lt = l
            gt = r
            while i <= gt:
                if nums[i] < c:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > c:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1
            if res < lt:
                r = lt - 1
            elif res > gt:
                l = gt + 1
            else:
                return nums[res]