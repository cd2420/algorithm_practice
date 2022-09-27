# 프로그래머스
# JadenCase 문자열 만들기

def checkFirstNumber(s):
    numbers = [str(i) for i in range(10)]
    if s[0] in numbers:
        return True
    else :
        return False
    

def solution(s):
    answer = ''
    
    s = s.lower()
    s_lst = list(s)
    while s_lst:
        word = s_lst.pop(0)
        if word == ' ':
            answer += word
            continue
        if checkFirstNumber(word):
            answer += word
            while s_lst and s_lst[0] != ' ':
                answer += s_lst.pop(0)
        else :
            answer += word.upper()
            while s_lst and s_lst[0] != ' ':
                answer += s_lst.pop(0)
        
    
    return answer