class Solution:
    def decodeString(self, s):
        stack = []
        num = 0
        res = ""
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            elif i == "[":
                stack.append((res, num))
                res = ""
                num = 0
            elif i == "]":
                temp, k = stack.pop()
                res = temp + res * k
            else:
                res += i
        return res