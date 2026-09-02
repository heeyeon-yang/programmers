def solution(sides):
    max_side = max(sides)
    total = sum(sides)
    
    if max_side < total - max_side:
        return 1
    else:
        return 2