def solution(a, b, c):
    case01 = a + b + c
    case02 = case01 * (a**2 + b**2 + c**2)
    case03 = case02 * (a**3 + b**3 + c**3)    
    
    if a == b == c:
        return case03
    elif a != b and b != c and a != c:
        return case01
    else:
        return case02
       