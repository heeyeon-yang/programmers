def solution(num_list):
    count_odd = 0
    count_even = 0
    
    for i in num_list:
        if i % 2 == 1:
            count_odd += 1
        else:
            count_even += 1
            
    return [count_even, count_odd]