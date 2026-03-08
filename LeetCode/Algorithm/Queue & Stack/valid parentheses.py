class Solution:
    def isValid(self, s):
        stack = []
        temp = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in temp:
                if not stack or stack[-1] != temp[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0