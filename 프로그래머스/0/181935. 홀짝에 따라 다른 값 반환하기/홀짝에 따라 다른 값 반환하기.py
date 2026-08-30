def solution(n):
    odd_sum = 0
    even_sum = 0
    
    if n % 2 == 1:
        for i in range(1, n+1, 2):
            odd_sum += i
        return odd_sum
    
    else:
        for i in range(2, n+1, 2):
            even_sum += i ** 2
        return even_sum
    