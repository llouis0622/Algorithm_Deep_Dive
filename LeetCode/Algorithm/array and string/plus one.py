class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = len(digits)
        for i in range(num - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits