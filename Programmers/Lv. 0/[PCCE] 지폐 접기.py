def solution(wallet, bill):
    normal = 0
    rotate = 0
    num_normal = bill[:]
    while num_normal[0] > wallet[0] or num_normal[1] > wallet[1]:
        if num_normal[0] > num_normal[1]:
            num_normal[0] //= 2
        else:
            num_normal[1] //= 2
        normal += 1
    num_rotate = [bill[1], bill[0]]
    while num_rotate[0] > wallet[0] or num_rotate[1] > wallet[1]:
        if num_rotate[0] > num_rotate[1]:
            num_rotate[0] //= 2
        else:
            num_rotate[1] //= 2
        rotate += 1
    return min(normal, rotate)