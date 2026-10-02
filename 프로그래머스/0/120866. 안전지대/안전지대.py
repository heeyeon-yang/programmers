def solution(board):
    n = len(board)
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 0), (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    
    dangers = set()
    
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    
                    if 0 <= nr < n and 0 <= nc < n:
                        dangers.add((nr, nc))
                        
    return (n*n) - len(dangers)
            