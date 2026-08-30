def solution(num_list):
    mult = 1
    square = 0
    
    for num in num_list:
        mult *= num
        square += num
        
    if mult < (square ** 2) :
            return 1
    else:
            return 0