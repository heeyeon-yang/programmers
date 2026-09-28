def solution(park, routes):
    H = len(park)
    W = len(park[0])
    
    r, c = 0, 0 
    
    # 시작 위치 찾기
    for row_idx, row in enumerate(park):
        for col_idx, char in enumerate(row): 
            if char == 'S':
                r, c = row_idx, col_idx
                break  
        if park[r][c] == 'S':
            break 
            
    dics = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)
    }
    
    for route in routes:
        op, n_str = route.split() 
        n = int(n_str)            
        dr, dc = dics[op]
        is_valid = True
        
        for step in range(1, n + 1):
            check_r = r + dr * step
            check_c = c + dc * step
            
            if not (0 <= check_r < H and 0 <= check_c < W) or park[check_r][check_c] == 'X':
                is_valid = False
                break
                
        if is_valid:
            r = r + dr * n
            c = c + dc * n
            
    return [r, c]
        