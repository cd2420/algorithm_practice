def dfs(start, tickets, tmp, result_len):

    dept_list = []
    for i in range(len(tickets)):
        ticket = tickets[i]
        if start == ticket[0]:
            dept_list.append((ticket[1], i))

    if len(dept_list) == 0:
        return tmp
    else:
        dept_list.sort()

    for dept, idx in dept_list:
        ticket = tickets.pop(idx)
        tmp.append(dept)
        check = dfs(dept, tickets, tmp, result_len)
        if check:
            if len(check) == result_len:
                return tmp
        tickets.insert(idx, ticket)
        tmp.pop()


def solution(tickets):
    answer = []
    result_len = len(tickets) + 1
    answer = dfs("ICN", tickets, ["ICN"], result_len)
    return answer
