from collections import Counter

def solution(N, stages):
    fail_rates = {}
    total_players = len(stages)
    stage_counts = Counter(stages)
    
    for stage in range(1, N + 1):
        if total_players > 0:
            count = stage_counts[stage]
            
            fail_rates[stage] = count / total_players
            total_players -= count            
        else:
            fail_rates[stage] = 0
            
    result = sorted(fail_rates, key=lambda x: fail_rates[x], reverse=True)
    
    return result