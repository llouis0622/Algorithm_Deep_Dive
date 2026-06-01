class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        ans = 0
        for i in arr:
            while stack[-1] <= i:
                m = stack.pop()
                ans += m * min(stack[-1], i)
            stack.append(i)
        while len(stack) > 2:
            ans += stack.pop() * stack[-1]
        return ans
