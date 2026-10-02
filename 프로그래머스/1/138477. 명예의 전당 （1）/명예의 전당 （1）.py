def solution(k, score):
    answer = []
    hof = []
    
    for s in score:
        hof.append(s)
        hof.sort(reverse=True)
        
        if len(hof) > k:
            hof.pop()
            
        answer.append(hof[-1])
        
    return answer