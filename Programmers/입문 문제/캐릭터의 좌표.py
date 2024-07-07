def solution(keyinput, board):
    ans = [0, 0]
    x = board[0] // 2
    y = board[1] // 2
    move_dict = {
        "up": [0, 1],
        "down": [0, -1],
        "left": [-1, 0],
        "right": [1, 0]
    }
    for i in keyinput:
        move = move_dict[i]
        arr = [ans[0] + move[0], ans[1] + move[1]]
        if -x <= arr[0] <= x and -y <= arr[1] <= y:
            ans = arr
    return ans