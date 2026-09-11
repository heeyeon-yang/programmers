def solution(my_string):
    targets = ['a', 'e', 'i', 'o', 'u']
    
    for target in targets:
        my_string = my_string.replace(target, '')
        
    return my_string