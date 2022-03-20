# 짝지어 제거하기

def solution(s):
    check = []
    for i in s:
        if check:
            if check[-1] != i:
                check.append(i)
            else:
                check.pop()
        else:
            check.append(i)

    if len(check) == 0:
        return 1
    else:
        return 0
