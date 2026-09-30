def to_sec(str_time):
    m, s = map(int, str_time.split(':'))
    return m * 60 + s

def to_str(sec):
    m = sec // 60
    s = sec % 60
    return f"{m:02d}:{s:02d}"


def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = to_sec(video_len)
    pos_sec = to_sec(pos)
    op_start_sec = to_sec(op_start)
    op_end_sec = to_sec(op_end)
    
    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec
    
    for command in commands:
        if command == 'prev':
            pos_sec = max(0, pos_sec - 10)
        elif command == 'next':
            pos_sec = min(video_len_sec, pos_sec + 10)
            
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
        
    return to_str(pos_sec)
            