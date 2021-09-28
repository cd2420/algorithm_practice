# N-Queen
result = 0


def back_tracking(n, tmp):
    global result
    if len(tmp) == n:
        result += 1
        return
    for i in range(n):
        if is_ok(tmp, i):
            tmp.append(i)
            back_tracking(n, tmp)
            tmp.pop()


def is_ok(tmp, col):

    rows = len(tmp)
    if rows == 0:
        return True
    else:
        for row in range(rows):
            if tmp[row] == col or (rows - row == abs(col - tmp[row])):
                return False
        return True


def solution(n):
    global result
    back_tracking(n, [])
    answer = result
    return answer
