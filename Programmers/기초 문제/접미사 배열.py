def solution(my_string):
    lst = []
    for i in range(len(my_string)):
        lst.append(my_string[i:])
    lst.sort()
    return lst