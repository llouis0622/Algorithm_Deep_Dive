import re

s = input()
reg = ["&&", r"\|\|", "<", ">", r"\(", r"\)", " "]
temp = '(' + '|'.join(reg) + ')'
res = re.split(temp, s)
ans = [t for t in res if t.strip() != ""]
print(' '.join(ans))