from collections import Counter

def solution(X, Y):
    answer = []
    count_X = Counter(X)
    count_Y = Counter(Y)
    
    for digit in map(str, range(9, -1, -1)):
        common = min(count_X[digit], count_Y[digit])
        answer.append(digit * common)
        
    result = ''.join(answer)
    
    if not result:
        return '-1'
    
    if result[0] == '0':
        return '0'
    
    return result
