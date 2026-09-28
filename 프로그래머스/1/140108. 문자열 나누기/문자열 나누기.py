def solution(s):
    answer, count_x, count_other = 0, 0, 0
    x = ''
    
    for char in s:
        if count_x == 0 and count_other == 0:
            x = char
            count_x = 1
            continue
            
        if char == x:
            count_x += 1
        else:
            count_other += 1
            
        if count_x == count_other:
            answer += 1
            count_x, count_other = 0, 0
            
    if count_x != 0 or count_other != 0:
        answer +=1
    
    return answer