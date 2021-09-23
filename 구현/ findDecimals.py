# 소수 찾기
from itertools import permutations


def solution(numbers):
    answer = 0
    check_set = set()
    for i in range(1, len(numbers) + 1):
        check = permutations(numbers, i)
        for c in check:
            insert_int = int(''.join(list(c)))
            check_set.add(insert_int)

    for i in check_set:

        count = 0
        for j in range(1, i + 1):
            if count > 2:
                break
            if i % j == 0:
                count += 1
        if count == 2:
            answer += 1
    return answer
