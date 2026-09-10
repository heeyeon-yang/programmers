def solution(rsp):
    answer = ''
    map_win = {'2':'0', '0':'5', '5':'2'}
    
    for ch in rsp:
        answer += map_win[ch]
        
    return answer