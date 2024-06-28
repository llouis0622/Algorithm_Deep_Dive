def solution(rsp):
    lst = {'2': '0', '0': '5', '5': '2'}
    ans = ''.join(lst[i] for i in rsp)
    return ans