def solution(t, p):
    answer = 0
    length = len(p)
    
    for i in range(len(t) - length + 1):
        sub_num = int(t[i:i+length])
        if sub_num <= int(p):
            answer += 1
    
    return answer