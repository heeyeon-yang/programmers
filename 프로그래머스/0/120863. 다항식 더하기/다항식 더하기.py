def solution(polynomial):
    coef, const = 0, 0
    result = []
    
    terms = polynomial.split(' + ')
    
    for term in terms:
        if 'x' in term:
            if term == 'x':
                coef += 1
            else:
                coef += int(term.replace('x', ''))
        else: const += int(term)
        
    
    if coef > 0:
        if coef == 1:
                result.append('x')
        else: result.append(f'{coef}x')
            
    if const > 0:
        result.append(str(const))
        
    return ' + '.join(result)