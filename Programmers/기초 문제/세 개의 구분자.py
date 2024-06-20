import re


def solution(myStr):
    ans = re.split('[abc]', myStr)
    ans = [i for i in ans if i]
    if not ans:
        return ["EMPTY"]
    return ans