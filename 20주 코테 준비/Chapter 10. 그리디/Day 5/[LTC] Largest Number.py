from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0
        
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))
        res = ''.join(nums)
        return '0' if res[0] == '0' else res
