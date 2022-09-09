# 프로그래머스
# 풍선 터뜨리기
def solution(a):
    answer = 2
    if len(a) <= 2:
        return len(a)
    
    left_min = a[0]
    right_min = a[-1]
    visited = [False] * len(a)
    visited[0] = True
    visited[-1] = True
    for i in range(1, len(a)-1):
        
        if a[i] <= left_min :
            if not visited[i]:
                visited[i] = True
                answer += 1
            left_min = a[i]
    
    for i in range(len(a)-2, -1, -1):
        
        if a[i] <= right_min :
            if not visited[i]:
                visited[i] = True
                answer += 1
            right_min = a[i]
        
    return answer