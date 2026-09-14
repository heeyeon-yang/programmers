def solution(spell, dic):
    set_spell = set(spell)
    
    for word in dic:
        if set(word) == set_spell:
            return 1
        
    return 2