def solution(name, yearning, photo):
    answer = []
    
    score_dict = {}
    for i in range(len(name)):
        score_dict[name[i]] = yearning[i]
        
    for p in photo:
        total_score = 0
        
        for person in p:
            if person in score_dict:
                total_score += score_dict[person]
                
        answer.append(total_score)
    return answer