# 네트워크 연결
import sys
input = sys.stdin.readline


def find_parent(x):
    if x != tree[x]:
        x = find_parent(tree[x])
    return x


n = int(input())
m = int(input())
tree = {}
for i in range(1, n + 1):
    tree[i] = i

graph = [list(map(int, input().split())) for _ in range(m)]
graph.sort(key=lambda x: x[2])

result = 0
for a, b, c in graph:
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        if a > b:
            tree[a] = b
        else:
            tree[b] = a
        result += c
print(result)
