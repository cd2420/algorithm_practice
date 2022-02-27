# 괄혼 추가하기

def calculate(calculate_idx_lst):
    tmp_nums = []
    idx = 0
    while idx < n:
        if idx not in calculate_idx_lst:
            tmp_nums.append(nums[idx])
            idx += 1
        else:
            x = tmp_nums.pop()
            func = nums[idx]
            y = nums[idx + 1]

            if func == '*':
                tmp_nums.append(int(x) * int(y))
            elif func == '+':
                tmp_nums.append(int(x) + int(y))
            elif func == '-':
                tmp_nums.append(int(x) - int(y))
            idx += 2

    while len(tmp_nums) != 1:
        x = tmp_nums.pop(0)
        func = tmp_nums.pop(0)
        y = tmp_nums.pop(0)
        data = 0
        if func == '*':
            data = (int(x) * int(y))
        elif func == '+':
            data = (int(x) + int(y))
        elif func == '-':
            data = (int(x) - int(y))
        tmp_nums.insert(0, data)
    return tmp_nums[0]


def back_tracking(check_graph, check_cnt, start_idx):
    global result
    if len(check_graph) == check_cnt:
        result = max(result, calculate(check_graph))
        return
    for i in range(start_idx, n, 2):
        if check_graph:
            if check_graph[-1] + 2 == i:
                continue
        check_graph.append(i)
        back_tracking(check_graph, check_cnt, i)
        check_graph.pop()


n = int(input())
nums = list(input())
cnt = n // 2
result = -999999999999999
if n == 1:
    print(int(nums[0]))
else:
    for i in range(1, cnt + 1):
        back_tracking([], i, 1)
    print(result)
