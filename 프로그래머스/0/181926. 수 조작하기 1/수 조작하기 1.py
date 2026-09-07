def solution(n, control):
    
    for ch in control:
        if ch == 'w':
            n += 1
        elif ch == 's':
            n -= 1
        elif ch == 'd':
            n += 10
        elif ch == 'a':
            n -= 10
            
    return n