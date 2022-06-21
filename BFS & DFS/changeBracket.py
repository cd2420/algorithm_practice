# 프로그래머스
# 괄호변환
def solution(p):
    answer = ''
    p_list = list(p)
    if len(p_list) <= 0:
        return answer
    check = [0, 0]
    checkWord(p_list[0], check)
    
    idx = 1
    while len(p_list) > idx and check[0] != check[1]:
        checkWord(p_list[idx], check)
        idx += 1
    u = p_list[:idx]
    v = p_list[idx:]
    if isCorrectWord(u):
        answer += ''.join(u)
        answer += solution(''.join(v))
    else :
        correct = "("
        correct += solution(''.join(v))
        correct += ")"

        if u:
            u.pop(0)
        if u:
            u.pop()        
        
        answer = correct + change(u)
        
    return answer

def checkWord(w, check):
    if w == '(':
        check[0] += 1
    else :
        check[1] += 1
        
def isCorrectWord(u):
    if not u:
        return False
    x = u[0]
    if x != "(":
        return False
    cnt = 1
    idx = 1
    while cnt >= 0 and len(u) > idx :
        x = u[idx]
        if x == "(":
            cnt += 1
        else :
            cnt -= 1
        idx += 1
        
    if cnt == 0:
        return True
    else :
        return False

def change(u):
    returnValue = ""
    while u:
        x = u.pop(0)
        if x == "(":
            returnValue += ")"
        else:
            returnValue += "("
    return returnValue

print(solution("()))((()"))
