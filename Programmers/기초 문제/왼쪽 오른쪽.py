def solution(str_list):
    for i, j in enumerate(str_list):
        if j == "l":
            return str_list[:i]
        elif j == "r":
            return str_list[i+1:]
    return []