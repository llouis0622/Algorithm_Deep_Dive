def solution(data, ext, val_ext, sort_by):
    ext_idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}[ext]
    sort_idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}[sort_by]
    filtered_data = [row for row in data if row[ext_idx] < val_ext]
    sorted_data = sorted(filtered_data, key=lambda x: x[sort_idx])
    return sorted_data