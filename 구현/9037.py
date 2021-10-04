def check_is_same(graph):
    n = len(graph)
    for i in range(n - 1):
        if graph[i] != graph[i + 1]:
            return False
    return True


def make_all_even(graph):
    for i in range(len(graph)):
        if graph[i] % 2 != 0:
            graph[i] += 1


for _ in range(int(input())):
    n = int(input())
    candy = list(map(int, input().split()))
    count = 0
    make_all_even(candy)
    is_same = check_is_same(candy)

    while not is_same:
        count += 1

        tmp_lst = [0] * n
        for i in range(n):

            if candy[i] % 2 != 0:
                candy[i] += 1
            candy[i] = candy[i] // 2
            if i != n - 1:
                tmp_lst[i+1] = candy[i]
            else:
                tmp_lst[0] = candy[i]

        for i in range(n):
            candy[i] += tmp_lst[i]

        make_all_even(candy)
        is_same = check_is_same(candy)

    print(count)
