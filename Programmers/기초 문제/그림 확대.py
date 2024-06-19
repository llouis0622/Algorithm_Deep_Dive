def solution(picture, k):
    ans = []
    for i in picture:
        file = ''.join(j * k for j in i)
        for _ in range(k):
            ans.append(file)
    return ans