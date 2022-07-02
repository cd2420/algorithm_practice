# 여행 계획

def find_parent(x):
    if x == tree[x]:
        return x
    else :
        a = find_parent(tree[x])
        tree[x] = a
        return a

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        return
    else :
        if a > b:
            tree[a] = b
        else :
            tree[b] = a

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
check = list(map(int, input().split()))

tree = {}
for i in range(n):
    tree[i] = i

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(i, j)

result = tree[min(check)]
for c in check:
    if result != tree[c]:
        print('NO')
        break
else :
    print('YES')
    