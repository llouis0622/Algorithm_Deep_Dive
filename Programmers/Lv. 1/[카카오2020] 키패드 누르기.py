def solution(numbers, hand):
    key = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    left = key['*']
    right = key['#']
    res = []
    hand_use = 'R' if hand == 'right' else 'L'

    def get_distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    for num in numbers:
        if num in [1, 4, 7]:
            res.append('L')
            left = key[num]
        elif num in [3, 6, 9]:
            res.append('R')
            right = key[num]
        else:
            dist_l = get_distance(left, key[num])
            dist_r = get_distance(right, key[num])
            if dist_l < dist_r:
                res.append('L')
                left = key[num]
            elif dist_r < dist_l:
                res.append('R')
                right = key[num]
            else:
                res.append(hand_use)
                if hand_use == 'L':
                    left = key[num]
                else:
                    right = key[num]
    return ''.join(res)