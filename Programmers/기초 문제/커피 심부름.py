def solution(order):
    ans = 0
    for i in order:
        if i in ["iceamericano", "americanoice", "hotamericano", "americanohot", "americano", "anything"]:
            ans += 4500
        elif i in ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]:
            ans += 5000
    return ans