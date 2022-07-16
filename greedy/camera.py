# 프로그래머스
# 단속 카메라
def solution(routes):
    answer = 1
    routes.sort(reverse=True)
    
    s,e = routes.pop()
    while routes:
        n_s, n_e = routes.pop()
        if s <= n_s <= e:
            s = n_s
            e = min(e, n_e)
        else :
            answer += 1
            s, e = n_s, n_e
    return answer