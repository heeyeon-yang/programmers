def solution(num_list):
    total_sum = 0
    total_product =  1
    
    for num in num_list:
        total_sum += num
        total_product *= num
    
    if len(num_list) >= 11:
        return total_sum
    else:
        return total_product