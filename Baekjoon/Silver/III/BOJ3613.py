import sys

s = sys.stdin.readline().strip()


def cpp(x):
    if not x or x[0] == '_' or x[-1] == '_' or '__' in x:
        return False
    for i in x:
        if i == '_':
            continue
        if 'A' <= i <= 'Z':
            return False
        if not ('a' <= i <= 'z'):
            return False
    return True


def java(x):
    if not x or '_' in x:
        return False
    if not ('a' <= x[0] <= 'z'):
        return False
    for i in x:
        if not (('a' <= i <= 'z') or ('A' <= i <= 'Z')):
            return False
    return True


def cpp2java(x):
    temp = x.split('_')
    res = [temp[0]]
    for p in temp[1:]:
        res.append(p[0].upper() + p[1:] if p else '')
    return ''.join(res)


def java2cpp(x):
    ans = []
    for i in x:
        if 'A' <= i <= 'Z':
            ans.append('_')
            ans.append(i.lower())
        else:
            ans.append(i)
    return ''.join(ans)


if '_' in s and any('A' <= c <= 'Z' for c in s):
    print("Error!")
elif cpp(s):
    print(cpp2java(s))
elif java(s):
    print(java2cpp(s))
else:
    print("Error!")