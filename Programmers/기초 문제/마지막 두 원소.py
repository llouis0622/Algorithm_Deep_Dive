def solution(num_list):
    ans = num_list
    if num_list[-1] > num_list[-2]:
        ans.append(num_list[-1] - num_list[-2])
    else:
        ans.append(num_list[-1] * 2)
    return ans