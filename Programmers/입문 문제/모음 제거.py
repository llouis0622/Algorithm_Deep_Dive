def solution(my_string):
    str = "aeiou"
    return ''.join([i for i in my_string if i not in str])