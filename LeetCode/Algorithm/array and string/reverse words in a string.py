class Solution:
    def reverseWords(self, s):
        A = s.split()
        A.reverse()
        return " ".join(A)