class Solution:
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        num = 0
        A = []
        while i >= 0 or j >= 0 or num:
            s = num
            if i >= 0:
                s += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                s += ord(b[j]) - ord('0')
                j -= 1
            A.append(str(s % 2))
            num = s // 2
        return ''.join(reversed(A))