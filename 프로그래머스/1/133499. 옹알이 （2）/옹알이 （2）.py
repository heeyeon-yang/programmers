def is_valid(word, speak):
    for sound in speak:
        if sound * 2 in word:
            return False
        
    for sound in speak:
        word = word.replace(sound, ' ')
        
    return word.replace(' ', '') == ''
    
def solution(babbling):
    speak = ["aya", "ye", "woo", "ma"]
    return sum(1 for word in babbling if is_valid(word, speak))