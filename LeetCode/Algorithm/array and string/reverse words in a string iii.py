class Solution:
    def reverseWords(self, s):
        A = s.split(" ")
        for i in range(len(A)):
            A[i] = A[i][::-1]
        return " ".join(A)