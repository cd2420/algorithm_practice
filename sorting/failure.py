# 프로그래머스
# 실패율
def solution(N, stages):
    answer = []
    tmp = []
    check = [0] * (N+1)
    for s in stages:
        if s != N+1:
            check[s] += 1
    person = len(stages)
    for i in range(1, N+1):

        if check[i]:
            tmp.append((check[i] / person * 100, i))
            person -= check[i]
        else :
            tmp.append((0, i))

    if tmp:
        tmp.sort(key=lambda x:(-x[0], x[1]))
    for t in tmp:
        answer.append(t[1])
        
    return answer