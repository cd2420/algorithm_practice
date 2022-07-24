# 프로그래머스
# 코딩테스트 실전 대비 모의고사 2번
from copy import deepcopy
def solution(want, number, discount):
    answer = 0
    check = {}
    for i in range(len(want)):
        check[want[i]] = number[i]
    
    n = len(discount)
    for i in range(n):
        if i + 10 > n:
            break
        tmp_check = deepcopy(check)
        for j in range(i, i+10):
            stock = discount[j]
            if stock not in check:
                break
            tmp_check[stock] -= 1
        else:
            for key in tmp_check:
                if tmp_check[key] > 0:
                    break
            else :
                answer += 1
    return answer