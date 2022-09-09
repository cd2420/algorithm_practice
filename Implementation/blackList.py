# 프로그래머스
# 불량사용자
from itertools import permutations

def checkIsFalse(banned, user):
    if len(banned) != len(user):
        return True
    
    size = len(banned)
    for i in range(size):
        if banned[i] == "*" or banned[i] == user[i]:
            continue
        else :
            return True
    return False

def solution(user_id, banned_id):
    result = []

    for banned in banned_id:
        size = len(banned)
    for i in permutations(user_id, len(banned_id)):
        tmp_user = list(i)
        
        for idx in range(len(banned_id)):
            if checkIsFalse(banned_id[idx], tmp_user[idx]):
                break
        else :
            set_tmp_user = set(tmp_user)
            if set_tmp_user not in result:
                result.append(set_tmp_user)
    return len(result)