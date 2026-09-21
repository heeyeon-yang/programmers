def solution(nums):
    pick = len(nums) // 2
    types = len(set(nums))
    
    return min(pick, types)