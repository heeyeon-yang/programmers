def solution(i, j, k):
    total = ''
    target = str(k)
    
    for num in range(i, j+1):
        total += str(num)
        
    return total.count(target)