def back_tracking(n, cand):
    if len(cand) == n - 1:
        result.append(cand[:])
        return
    for i in range(4):
        if is_ok(i, cand):
            cand.append(func_mapper[i])
            back_tracking(n, cand)
            cand.pop()


def is_ok(check_func, cand):
    count = 0
    for c in cand:
        if func_mapper[check_func] == c:
            count += 1
    if count >= func_num[check_func]:
        return False
    else:
        return True


n = int(input())
num_lst = list(map(int, input().split()))
func_num = list(map(int, input().split()))
func_mapper = ['+', '-', '*', '//']

result = []
back_tracking(n, [])
max_result = -1e9
min_result = 1e9
for r in result:

    tmp_num_func = []
    for i in range(len(r)):
        tmp_num_func.append(num_lst[i])
        tmp_num_func.append(r[i])
    tmp_num_func.append(num_lst[-1])
    tmp_total_num = tmp_num_func[0]
    for i in range(1, len(tmp_num_func), 2):
        if tmp_num_func[i] == '+':
            tmp_total_num += tmp_num_func[i + 1]
        elif tmp_num_func[i] == '-':
            tmp_total_num -= tmp_num_func[i + 1]
        elif tmp_num_func[i] == '*':
            tmp_total_num *= tmp_num_func[i + 1]
        else:
            if tmp_total_num < 0:
                tmp_total_num = (-1 * tmp_total_num) // tmp_num_func[i + 1]
                tmp_total_num = -1 * tmp_total_num
            else:
                tmp_total_num //= tmp_num_func[i + 1]

    max_result = max(max_result, tmp_total_num)
    min_result = min(min_result, tmp_total_num)

print(max_result)
print(min_result)
