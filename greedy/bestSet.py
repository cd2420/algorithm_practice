# 프로그래머스
# 최고의 집합
def solution(n, s):
    answer = []
    if s <= 1 or n > s:
        return [-1]
    for i in range(n, 0, -1):
        check = s // i
        answer.append(check)
        s -= check
    answer.sort()
    return answer