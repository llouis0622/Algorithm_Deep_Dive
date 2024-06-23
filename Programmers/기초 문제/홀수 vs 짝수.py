def solution(num_list):
    odd = sum(num_list[0::2])
    even = sum(num_list[1::2])
    return max(odd, even)