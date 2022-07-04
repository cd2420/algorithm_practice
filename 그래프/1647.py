# 도시 분할 계획

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return x

def union_parent(a, b):
    if a > b:
        parent[a] = b
    else :
        parent[b] = a

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
graph.sort(key=lambda x:x[2])
parent = [i for i in range(n+1)]

result = 0
max_cnt = -1
for a, b, c in graph:
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        union_parent(a , b)
        result += c
        max_cnt = max(max_cnt, c)

print(result - max_cnt)