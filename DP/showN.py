# 프로그래머스
# N으로 표현

def sol(N, dp, number, cnt):

    if cnt > 8 :
        return -1
    if number == int(str(N) * cnt):
        return cnt
    dp[cnt].add(int(str(N) * cnt))
    
    for i in range(cnt-1, 0, -1):
        j = cnt - i
        for num2 in dp[i]:
            for num1 in dp[j]:
                if number == num1 + num2:
                    return cnt
                else :
                    dp[cnt].add(num1 + num2)

                if number == num1 * num2:
                    return cnt
                else :
                    dp[cnt].add(num1 * num2)

                if number == num1 - num2:
                    return cnt
                else :
                    dp[cnt].add(num1 - num2)
                if num2 > 0:
                    if number == num1 // num2:
                        return cnt
                    else :
                        dp[cnt].add(num1 // num2)

    return sol(N, dp, number, cnt + 1)

def solution(N, number):
    dp = [set() for _ in range(9)]
    answer = sol(N, dp, number, 1)
    return answer


print(solution(5, 12))