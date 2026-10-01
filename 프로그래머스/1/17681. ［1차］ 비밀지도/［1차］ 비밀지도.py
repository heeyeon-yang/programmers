def solution(n, arr1, arr2):
    answer = []
    
    for num1, num2 in zip(arr1, arr2):
        combined = num1 | num2      
        str_binary = bin(combined)[2:].zfill(n)
        row = str_binary.replace('1', '#').replace('0', ' ')
        answer.append(row)
    return answer