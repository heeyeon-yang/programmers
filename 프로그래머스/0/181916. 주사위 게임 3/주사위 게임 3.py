def solution(a, b, c, d):
    dice = [a,b,c,d]
    counts = {}
    
    for num in dice:
        counts[num] = counts.get(num, 0) + 1
        
    keys = list(counts.keys())
    
    if len(counts) == 1:
        return 1111 * keys[0]
    
    elif len(counts) == 2:
        if counts[keys[0]] == 3:
            p, q = keys[0], keys[1]
            return (10 * p + q) ** 2
        elif counts[keys[1]] == 3:
            p, q = keys[1], keys[0]
            return (10 * p + q) ** 2
        else: 
            p, q = keys[0], keys[1]
            return (p + q) * abs(p - q)
            
    elif len(counts) == 3:
        q, r = [k for k, v in counts.items() if v == 1]
        return q * r
        
    else:
        return min(dice)