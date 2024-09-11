def solution(sizes):
    width = 0
    height = 0
    for w, h in sizes:
        width_etc, height_etc = max(w, h), min(w, h)
        width = max(width, width_etc)
        height = max(height, height_etc)
    return width * height