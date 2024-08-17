def solution(nums):
    arr = set(nums)
    if len(nums) / 2 >= len(arr):
        return len(arr)
    else:
        return len(nums) / 2