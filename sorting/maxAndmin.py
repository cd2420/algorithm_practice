# 프로그래머스
# 최댓값과 최솟값
def solution(s):
    s_lst = list(map(int, s.split()))
    s_lst.sort()
    min_n = s_lst[0]
    max_n = s_lst[-1]
    answer = str(min_n) + ' ' + str(max_n)
    
    return answer