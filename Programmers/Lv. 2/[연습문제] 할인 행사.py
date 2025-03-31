from collections import Counter


def solution(want, number, discount):
    temp = dict(zip(want, number))
    ans = 0
    total = len(discount)
    for i in range(total - 9):
        num = discount[i:i + 10]
        counter = Counter(num)
        if all(counter[item] == temp[item] for item in temp):
            ans += 1
    return ans