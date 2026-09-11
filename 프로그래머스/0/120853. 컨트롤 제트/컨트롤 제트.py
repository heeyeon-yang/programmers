def solution(s):
    stack = []
    
    for str in s.split():
        if str == 'Z':
            stack.pop()
        else:
            stack.append(int(str))
            
    return sum(stack)