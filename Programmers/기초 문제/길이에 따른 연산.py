def solution(num_list):
    ans = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for num in num_list:
            ans = ans * num

        return ans