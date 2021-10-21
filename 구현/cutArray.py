# n ^ 2 배열자르기
def solution(n, left, right):

    left_side = left // n
    left_list = []
    for i in range(left_side):
        left_list.append(left_side + 1)
    for i in range(left_side, n):
        left_list.append(i + 1)

    right_side = right // n
    if left_side != right_side:

        left_list = left_list[left % n:]
        right_list = []
        for i in range(right_side):
            right_list.append(right_side + 1)
        for i in range(right_side, n):
            right_list.append(i + 1)
        right_list = right_list[:right % n + 1]

        for side in range(left_side + 1, right_side):
            for i in range(side):
                left_list.append(side + 1)
            for i in range(side, n):
                left_list.append(i + 1)

        left_list.extend(right_list)
    else:
        left_list = left_list[left % n: right % n + 1]
    return left_list
