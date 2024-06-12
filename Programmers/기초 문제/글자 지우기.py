def solution(my_string, indices):
    ans = []
    for i in range(len(my_string)):
        if i not in set(indices):
            ans.append(my_string[i])
    return ''.join(ans)