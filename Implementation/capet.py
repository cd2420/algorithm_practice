# 프로그래머스
# 카펫
def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            c = yellow // i
            if i < c :
                continue
            if i * 2 + c * 2 + 4 == brown:
                answer = [i+2, c+2]
                break
    return answer