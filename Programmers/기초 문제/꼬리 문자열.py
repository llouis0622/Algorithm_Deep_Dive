def solution(str_list, ex):
    return ''.join([i for i in str_list if ex not in i])