def solution(code):
    mode = 0
    ret = ''
    
    for idx, char in enumerate(code):
        if char == '1':
            mode = 1-mode
        else:
            if idx % 2 == mode:
                ret += char
                
    return ret if ret else 'EMPTY'
                