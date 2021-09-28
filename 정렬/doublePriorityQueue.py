# 이중 우선순위 큐
import heapq


def solution(operations):
    answer = []
    tmp_answer = []
    max_value_check = []
    min_value_check = []
    for operation in operations:
        if operation[0] == "I":
            num = int(operation[2:])
            tmp_answer.append(num)
            heapq.heappush(max_value_check, -1 * num)
            heapq.heappush(min_value_check, num)

        if operation[0] == "D":
            if operation[2:] == "1" and max_value_check:
                num = heapq.heappop(max_value_check) * -1
                tmp_answer.remove(num)
                min_value_check.remove(num)
            elif operation[2:] == "-1" and min_value_check:
                num = heapq.heappop(min_value_check)
                tmp_answer.remove(num)
                max_value_check.remove(num * -1)
    if len(tmp_answer) == 0:
        return [0, 0]
    else:
        answer.append(max(tmp_answer))
        answer.append(min(tmp_answer))
    return answer
