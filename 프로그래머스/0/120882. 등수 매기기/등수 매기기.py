def solution(score):
    total = [eng + math for eng, math in score]
    sorted_total = sorted(total, reverse = True)
    answer = [sorted_total.index(t) + 1 for t in total]
    
    return answer