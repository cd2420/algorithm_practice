# 이진 변환 반복하기
def trans_2(c):
    string = ''
    while c > 1:
        string = str(c % 2) + string
        c //= 2
    string = str(c) + string
    return string


def solution(s):

    check_zero = 0
    count = 0
    while len(s) > 1:
        check_zero += s.count('0')
        s = s.replace('0', '')
        c = len(s)
        s = trans_2(int(c))
        count += 1
    answer = [count, check_zero]
    return answer
