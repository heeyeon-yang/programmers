def solution(dots):
    width = max(dot[0] for dot in dots) - min(dot[0] for dot in dots)
    height = max(dot[1] for dot in dots) - min(dot[1] for dot in dots)
    
    return width * height