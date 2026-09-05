def solution(sides):
    x, y = sorted(sides)
    # b가 가장 클 때
    case1 = len(range(y-x+1, y+1))
    # 새 값이 가장 클 때
    case2 = len(range(y+1, x+y))
    
    return case1 + case2