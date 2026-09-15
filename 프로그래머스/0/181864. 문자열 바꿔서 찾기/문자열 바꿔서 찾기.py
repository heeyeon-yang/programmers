def solution(myString, pat):
    newString = myString.replace('A', 'X').replace('B', 'A').replace('X', 'B')
    return 1 if pat in newString else 0