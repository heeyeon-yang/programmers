def solution(x):
    sum_digit = sum(int(c) for c in str(x))
    return x % sum_digit == 0