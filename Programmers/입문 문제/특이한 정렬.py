def solution(numlist, n):
    for i in range(len(numlist)):
        for j in range(i + 1, len(numlist)):
            if abs(numlist[i] - n) > abs(numlist[j] - n) or (abs(numlist[i] - n) == abs(numlist[j] - n) and numlist[i] < numlist[j]):
                numlist[i], numlist[j] = numlist[j], numlist[i]
    return numlist