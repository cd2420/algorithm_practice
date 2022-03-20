# 수식 최대화

def find_func(expression, check_func, func):

    for check in check_func:
        if check in expression:
            func.append(check)


def is_ok(cand, i):
    if i in cand:
        return False
    return True


def make_func(all_func, n, cand, func):
    if len(cand) == n:
        all_func.append(cand[:])
        return

    for i in func:
        if is_ok(cand, i):
            cand.append(i)
            make_func(all_func, n, cand, func)
            cand.pop()


def solution(expression):
    answer = 0
    func = []
    find_func(expression, ['+', '-', '*'], func)

    all_func = []
    make_func(all_func, len(func), [], func)

    split_expression = expression
    check_tmp = 0
    while check_tmp < len(split_expression):
        if split_expression[check_tmp] in func:
            split_expression = split_expression[:check_tmp] + ' ' + \
                split_expression[check_tmp] + ' ' + \
                split_expression[check_tmp+1:]
            check_tmp += 2
        check_tmp += 1

    split_expression = split_expression.split()
    result = []
    for func in all_func:
        tmp_split_expression = split_expression[:]
        for f in func:
            while f in tmp_split_expression:
                check_idx = tmp_split_expression.index(f)
                func_str = tmp_split_expression.pop(check_idx - 1) + tmp_split_expression.pop(
                    check_idx - 1) + tmp_split_expression.pop(check_idx - 1)
                tmp_split_expression.insert(check_idx - 1, str(eval(func_str)))
        result.append(tmp_split_expression[0])
    result = list(map(abs, list(map(int, result))))
    answer = max(result)
    return answer
