def solution(s, skip, index):
    answer = []
    valid_alphabets = [ch for ch in "abcdefghijklmnopqrstuvwxyz" if ch not in skip]
    
    for ch in s:
        idx = valid_alphabets.index(ch)
        new_idx = (idx + index) % len(valid_alphabets)
        
        answer.append(valid_alphabets[new_idx])
        
    return ''.join(answer)