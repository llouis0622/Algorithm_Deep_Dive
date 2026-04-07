def solution(array, commands):
    ans = []
    for op in commands:
        x, y, z = op
        arr = array[x - 1:y]
        arr.sort()
        ans.append(arr[z - 1])
    return ans
