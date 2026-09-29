def solution(n):
    rev_num = ''
    
    while n > 0:
        rev_num += str(n%3)
        n //= 3
        
    return int(rev_num, 3)