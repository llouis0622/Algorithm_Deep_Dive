def solution(A, B):
    if len(A) != len(B):
        return -1
    for i in range(len(A)):
        if A == B:
            return i
        A = A[-1] + A[:-1]
    return -1