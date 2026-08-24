def solution(players, callings):
    
    player_dict = {}
    for i in range(len(players)):
        name = players[i]
        player_dict[name] = i

    for name in callings:
        idx = player_dict[name]         
        front_player = players[idx - 1] 
        
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        
        player_dict[name] = idx - 1
        player_dict[front_player] = idx
        
    return players