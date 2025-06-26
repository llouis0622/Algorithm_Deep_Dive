def solution(numbers):
    ans = []
    for x in numbers:
        if x % 2 == 0:
            ans.append(x + 1)
        else:
            bit = bin(x)[2:]
            idx = bit.rfind('0')
            if idx == -1:
                ans.append(int('10' + bit[1:], 2))
            else:
                bit = list('0' + bit)
                i = len(bit) - 1
                while i > 0:
                    if bit[i - 1] == '0' and bit[i] == '1':
                        bit[i - 1], bit[i] = '1', '0'
                        break
                    i -= 1
                ans.append(int(''.join(bit), 2))
    return ans