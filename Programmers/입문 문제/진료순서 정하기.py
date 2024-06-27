def solution(emergency):
    lst = sorted(emergency, reverse=True)
    return [lst.index(i) + 1 for i in emergency]