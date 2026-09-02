def solution(s):
    single_dict = sorted([c for c in set(s) if s.count(c) == 1])
    return ''.join(single_dict)