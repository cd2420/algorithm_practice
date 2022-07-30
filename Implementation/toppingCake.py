# 프로그래머스
# 토핑
from collections import deque, defaultdict
def solution(topping):
    answer = 0

    left_dict = defaultdict(int)
    left_num = 0

    right = deque(topping)
    right_dict = defaultdict(int)
    for r in right:
        right_dict[r] += 1
    right_num = len(right_dict)
    while right:
        check = right.popleft()

        right_dict[check] -= 1
        if right_dict[check] == 0:
            right_num -= 1

        if left_dict[check] == 0:
            left_num += 1
        left_dict[check] += 1

        if left_num == right_num:
            answer += 1
    return answer