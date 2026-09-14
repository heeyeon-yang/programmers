def solution(arr):
    count = 0
    
    while True:
        new_arr = []
        
        for num in arr:
            if num >= 50 and num % 2 == 0:
                new_arr.append(num // 2)
            elif num < 50 and num % 2 == 1:
                new_arr.append(num * 2 + 1)
            else:
                new_arr.append(num)
                
        if arr == new_arr:
            return count
        
        arr = new_arr
        count += 1