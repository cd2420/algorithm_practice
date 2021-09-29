# 섬 연결하기
def find_parent(a, parent):
    if a == parent[a]:
        return a
    else:
        x = parent[a]
        return find_parent(x, parent)


def same_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a == b:
        return True
    else:
        return False


def union(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])

    tree = dict()
    parent = dict()

    for cost in costs:
        a, b, c = cost
        parent[a] = a
        parent[b] = b

    for cost in costs:
        a, b, c = cost
        if not same_parent(a, b, parent):
            answer += c
            union(a, b, parent)

    return answer
