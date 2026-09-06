def solution(intStrs, k, s, l):
    answer = []
    
    for num in intStrs:
        val = int(num[s:s+l])
        if val > k:
            answer.append(val)
            
    return answer