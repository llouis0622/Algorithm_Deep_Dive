def solution(wallpaper):
    min_row = float('inf')
    min_col = float('inf')
    max_row = float('-inf')
    max_col = float('-inf')
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                min_row = min(min_row, i)
                min_col = min(min_col, j)
                max_row = max(max_row, i)
                max_col = max(max_col, j)
    return [min_row, min_col, max_row + 1, max_col + 1]