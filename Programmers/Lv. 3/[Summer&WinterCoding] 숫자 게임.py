def solution(A, B):
    A.sort()
    B.sort()
    i = j = ans = 0
    n = len(A)
    while i < n and j < n:
        if B[j] > A[i]:
            ans += 1
            i += 1
            j += 1
        else:
            j += 1
    return ans