def solution(s):
    temp = list(map(int, s.split()))
    return f'{min(temp)} {max(temp)}'