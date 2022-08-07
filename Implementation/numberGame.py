# 프로그래머스
# 숫자게임
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    n = len(A)
    idx_A = 0
    idx_B = 0
    while idx_A < n and idx_B < n:
        if A[idx_A] >= B[idx_B]:
            idx_B += 1
        else :
            answer += 1
            idx_A += 1
            idx_B += 1
    
    return answer