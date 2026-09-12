def solution(strArr):
    counts = {}
    
    for s in strArr:
        length = len(s)
        counts[length] = counts.get(length, 0) +1
        
    return max(counts.values())