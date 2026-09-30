def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    current_health = health
    prev_time = 0
    
    for attack_time, damage in attacks:
        diff = attack_time - prev_time -1
        
        if diff > 0:
            heal = (diff * x) + (diff // t * y)
            current_health = min(max_health, heal + current_health)
        
        current_health -= damage
        
        if current_health <= 0:
            return -1
        
        prev_time = attack_time
        
    return current_health
    