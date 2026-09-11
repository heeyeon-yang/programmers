def solution(n):
    answer = 0
    
    for num in range(1, n+1):
        count = 0
        
        for num2 in range(1, num+1):
            if num % num2 == 0:
                count += 1
            if count == 3:
                answer += 1
                break
    
    return answer