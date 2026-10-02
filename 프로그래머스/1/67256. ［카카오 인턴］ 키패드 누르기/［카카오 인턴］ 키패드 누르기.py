def solution(numbers, hand):
    answer = ''
    
    pos = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1),
          6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2),
          '*': (3,0), 0: (3,1), '#': (3,2)}
    
    p_left = pos['*']
    p_right = pos['#']
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            p_left = pos[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            p_right = pos[num]
        else:
            p_target = pos[num]
            
            dist_left = abs(p_left[0] - p_target[0]) + abs(p_left[1] - p_target[1])
            dist_right = abs(p_right[0] - p_target[0]) + abs(p_right[1] - p_target[1])
            
            if dist_left < dist_right:
                answer += 'L'
                p_left = p_target
            elif dist_right < dist_left:
                answer += 'R'
                p_right = p_target
            else:
                if hand == 'left':
                    answer += 'L'
                    p_left = p_target
                else:
                    answer += 'R'
                    p_right = p_target
                    
    
    return answer