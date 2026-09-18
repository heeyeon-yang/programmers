def solution(my_string, is_prefix):
    length = len(is_prefix)
    
    return 1 if my_string[:length] == is_prefix else 0