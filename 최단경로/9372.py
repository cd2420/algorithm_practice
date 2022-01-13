# 상근이의 여행
def equal_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a == b:
        return True
    else:
        return False


def find_parent(x, parent):
    if x == parent[x]:
        return x
    else:
        y = find_parent(parent[x], parent)
        parent[x] = y
        return y


def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a > b:
        parent[a] = b
        tree[b] += tree[a]
    else:
        parent[b] = a
        tree[a] += tree[b]


for _ in range(int(input())):
    n, m = map(int, input().split())
    tree = {}
    parent = {}
    for i in range(1, n+1):
        tree[i] = 1
        parent[i] = i
    for __ in range(m):
        a, b = map(int, input().split())
        if not equal_parent(a, b, parent):
            union_parent(a, b, parent)
    print(tree[1] - 1)
