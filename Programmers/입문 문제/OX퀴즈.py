def solution(quiz):
    ans = []
    for i in quiz:
        arr, num = i.split('=')
        if eval(arr.strip()) == int(num.strip()):
            ans.append("O")
        else:
            ans.append("X")
    return ans