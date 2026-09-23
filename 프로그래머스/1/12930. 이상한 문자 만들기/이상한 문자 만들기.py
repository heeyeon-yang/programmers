def solution(s):
    result = []
    words = s.split(' ')
    
    for word in words:
        new_word = []
        for i, ch in enumerate(word):
            if i % 2 == 0:
                new_word.append(ch.upper())
            else:
                new_word.append(ch.lower())
        result.append(''.join(new_word))
         
    return ' '.join(result)