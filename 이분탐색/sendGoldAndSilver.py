# 프로그래머스
# 금과 은 운반하기
def solution(a, b, g, s, w, t):

    start = 1
    end = 4 * (10**9) * (10 ** 5)
    answer = 4 * (10**9) * (10 ** 5)
    size = len(g)
    while start <= end:
        mid = (start + end) // 2
        t_g = 0
        t_s = 0
        total = 0
        for i in range(size):
            cnt = mid // (t[i] * 2)
            if mid % (t[i] * 2) >= t[i]:
                cnt += 1
            check_g = w[i] * cnt if g[i] >= w[i] * cnt else g[i]
            check_s = w[i] * cnt if s[i] >= w[i] * cnt else s[i]
            check_total = check_g + check_s if check_g + check_s <= w[i] * cnt else w[i] * cnt
            
            t_g += check_g
            t_s += check_s
            total += check_total
        if t_g >= a and t_s >= b and total >= (a + b):
            answer = min(answer, mid)
            end = mid - 1
        else :
            start = mid + 1
            
    return answer