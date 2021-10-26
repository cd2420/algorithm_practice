# 보석 쇼핑
from collections import defaultdict


def solution(gems):
    answer = []
    result = defaultdict(int)
    result[gems[0]] = 1
    first = 0
    last = 0
    tmp = [0, len(gems)]
    check_len = len(set(gems))
    while first <= last and last < len(gems):
        if check_len != len(result):
            last += 1
            if last >= len(gems):
                break
            result[gems[last]] += 1
        else:
            if tmp[1] - tmp[0] > last - first:
                tmp = [first, last]
            result[gems[first]] -= 1
            if result[gems[first]] <= 0:
                del result[gems[first]]
            first += 1

    return [tmp[0] + 1, tmp[1] + 1]
