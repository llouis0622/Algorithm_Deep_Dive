def solution(skill, skill_trees):
    cnt = 0
    for t in skill_trees:
        check = ''.join([s for s in t if s in skill])
        if skill.startswith(check):
            cnt += 1
    return cnt