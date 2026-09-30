def solution(food):
    left = ''
    
    for i in range(1, len(food)):
        count = food[i] // 2
        left += str(i) * count
        
    return left + '0' + left[::-1]