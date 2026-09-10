def solution(my_string):
    answer = 0
    temp = ''
    
    for ch in my_string:
        if ch.isdigit():
            temp += ch
        else:
            if temp != '':
                answer += int(temp)
                temp = ''
                
              
    if temp != '':
        answer += int(temp)
    
    return answer