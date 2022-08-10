# 행성 터널
import heapq
def find_parent(x):
    if x == parent[x]:
        return x
    else :
        a = find_parent(parent[x])
        parent[x] = a
        return a

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        return True
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
    
    return False

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    graph[i].append(i)
parent = [i for i in range(n)]

sorted_x = sorted(graph, key=lambda x:x[0])
sorted_y = sorted(graph, key=lambda x:x[1])
sorted_z = sorted(graph, key=lambda x:x[2])
q = []
for i in range(len(graph) - 1):
    abs_x = abs(sorted_x[i][0] - sorted_x[i+1][0])
    heapq.heappush(q, (abs_x, (sorted_x[i][3], sorted_x[i+1][3])))

    abs_y = abs(sorted_y[i][1] - sorted_y[i+1][1])
    heapq.heappush(q, (abs_y, (sorted_y[i][3], sorted_y[i+1][3])))

    abs_z = abs(sorted_z[i][2] - sorted_z[i+1][2])
    heapq.heappush(q, (abs_z, (sorted_z[i][3], sorted_z[i+1][3])))
answer = 0
while q:
    cnt, check = heapq.heappop(q)
    a = check[0]
    b = check[1]
    if not union_parent(a, b):
        answer += cnt
print(answer)