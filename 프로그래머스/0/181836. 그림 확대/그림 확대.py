def solution(picture, k):
    answer = []
    
    for row in picture:
        rows = ''.join(char * k for char in row)
        for _ in range(k):
            answer.append(rows)
                          
    return answer
