def solution(todo_list, finished):
    ans = []
    for i, j in zip(todo_list, finished):
        if not j:
            ans.append(i)
    return ans