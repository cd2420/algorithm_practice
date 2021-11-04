# 예상 대진표
def makeRoundNum(x):
    if x % 2 == 0:
        return x // 2
    else:
        return x // 2 + 1


def solution(n, a, b):
    answer = 0
    while True:
        a = makeRoundNum(a)
        b = makeRoundNum(b)
        answer += 1
        if a == b:
            break
    return answer
