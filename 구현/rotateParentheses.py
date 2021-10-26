# 괄호 회전하기
def is_set(s_1, s_2):
    if (s_1 == '(' and s_2 == ')') or (s_1 == '[' and s_2 == ']') or (s_1 == '{' and s_2 == '}'):
        return True
    else:
        return False


def find_set_idx(std_s, s):
    check_idx = 0
    for i in range(len(s)):
        if std_s == s[i]:
            check_idx += 1

        if is_set(std_s, s[i]):
            check_idx -= 1
            if check_idx == 0:
                return i
    return -1


def is_correct(s):
    if len(s) <= 2:
        if len(s) <= 1:
            return False
        if is_set(s[0], s[1]):
            return True

    idx = find_set_idx(s[0], s)
    if idx == -1:
        return False
    elif idx == 1:
        if is_correct(s[2:]):
            return True
        else:
            return False
    else:
        if idx != len(s) - 1:
            if is_correct(s[1:idx]) and is_correct(s[idx + 1:]):
                return True
            else:
                return False
        else:
            if is_correct(s[1:idx]):
                return True
            else:
                return False


def solution(s):
    answer = -1
    count = 0
    tmp_s = s
    for _ in range(len(s)):
        if is_correct(tmp_s):

            count += 1
        tmp_s = tmp_s[1:] + tmp_s[0]

    answer = count

    return answer
