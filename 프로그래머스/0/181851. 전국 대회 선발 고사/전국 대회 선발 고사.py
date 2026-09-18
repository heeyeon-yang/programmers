def solution(rank, attendance):
    selected = []          
    
    for i in range(len(rank)):
        if attendance[i]:
            selected.append((rank[i], i))
            
    selected.sort()
    a = selected[0][1]
    b = selected[1][1]
    c = selected[2][1]
    
    return 10000 * a + 100 * b + c