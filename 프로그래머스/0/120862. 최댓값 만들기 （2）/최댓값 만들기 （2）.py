def solution(numbers):
    numbers.sort(reverse=True)
    
    max_pos = numbers[0] * numbers[1]
    max_neg = numbers[-1] * numbers[-2]
    
    return max_pos if max_pos > max_neg else max_neg