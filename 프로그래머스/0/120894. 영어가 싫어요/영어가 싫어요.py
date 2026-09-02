def solution(numbers):
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i, nums in enumerate(num_list):
        numbers = numbers.replace(nums, str(i))
        
    return int(numbers)