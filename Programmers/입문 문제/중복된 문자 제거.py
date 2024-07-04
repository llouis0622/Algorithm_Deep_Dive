def solution(my_string):
    ans = ""
    arr = set()
    for i in my_string:
        if i not in arr:
            ans += i
            arr.add(i)
    return ans