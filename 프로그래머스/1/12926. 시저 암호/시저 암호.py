def solution(s, n):
    answer = []
    
    for ch in s:
        if ch.isupper():
            new_ch = chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
            answer.append(new_ch)
        elif ch.islower():
            new_ch = chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
            answer.append(new_ch)
        else:
            answer.append(ch)
            
    return ''.join(answer)
            