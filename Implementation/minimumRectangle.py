# 최소 직사각형
def solution(sizes):
    answer = 0

    check_sizes = list(map(list, zip(*sizes)))
    max_len = max(max(check_sizes[0]), max(check_sizes[1]))

    other_len = -1
    for size in sizes:
        other_len = max(min(size), other_len)

    answer = max_len * other_len
    return answer
