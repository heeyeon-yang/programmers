def solution(my_string, overwrite_string, s):
    length = s + len(overwrite_string)
    
    return my_string[:s] + overwrite_string + my_string[length:]