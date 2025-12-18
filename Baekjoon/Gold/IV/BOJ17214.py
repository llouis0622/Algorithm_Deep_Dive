import sys

s = sys.stdin.readline().strip()


def check(coef, var):
    if coef == 0:
        return ""
    temp = "-" if coef < 0 else ""
    c = abs(coef)
    if var == "xx":
        if c == 1:
            return temp + "xx"
        return temp + str(c) + "xx"
    if var == "x":
        if c == 1:
            return temp + "x"
        return temp + str(c) + "x"
    return temp + str(c)


a = 0
b = 0
if "x" in s:
    idx = s.find("x")
    num = s[:idx]
    if num == "":
        a = 1
    elif num == "-":
        a = -1
    else:
        a = int(num)
    res = s[idx + 1:]
    if res != "":
        b = int(res)
else:
    b = int(s)
cur = []
k = a // 2
t1 = check(k, "xx")
if t1:
    cur.append(t1)
t2 = check(b, "x")
if t2:
    cur.append(t2)
if not cur:
    ans = "W"
else:
    ans = cur[0]
    for t in cur[1:]:
        if t[0] == "-":
            ans += t
        else:
            ans += "+" + t
    ans += "+W"
print(ans)