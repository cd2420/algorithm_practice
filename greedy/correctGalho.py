# 프로그래머스
# 올바른 괄호
def solution(s):
    
    n = len(s)
    check = 0
    for i in range(n):
        if s[i] == "(":
            check += 1
        else :
            check -= 1
        if check < 0:
            return False
    
    return True if check == 0 else False