def solution(babbling):
    answer = 0
    words = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        for w in words:
                word = word.replace(w, ' ')
        
        if word.strip() == '':
            answer += 1
            
    return answer