def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        sub = [x for x in arr[s:e+1] if x > k]
        if sub:
            answer.append(min(sub))
        else:
            answer.append(-1)
            
    return answer