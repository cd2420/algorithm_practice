# 점프와 순간이동
def solution(n):
    ans = 0

    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            count += 1
    ans = count + 1
    return ans
