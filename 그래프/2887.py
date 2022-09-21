# 행성 터널
import heapq

def find_parent(x):
    if parent[x] == x:
        return x
    else :
        a = find_parent(parent[x])
        parent[x] = a
        return a


N = int(input())
dist = [list(map(int, input().split())) for _ in range(N)]
dist = list(enumerate(dist))
parent = [i for i in range(N)]

dist_x = sorted(dist, key= lambda x:x[1][0])
dist_y = sorted(dist, key= lambda x:x[1][1])
dist_z = sorted(dist, key= lambda x:x[1][2])
q = []
for i in range(1, N):
    x = dist_x[i][1][0] - dist_x[i-1][1][0]
    q.append((x, (dist_x[i][0], dist_x[i-1][0])))

    y = dist_y[i][1][1] - dist_y[i-1][1][1]
    q.append((y, (dist_y[i][0], dist_y[i-1][0])))

    z = dist_z[i][1][2] - dist_z[i-1][1][2]
    q.append((z, (dist_z[i][0], dist_z[i-1][0])))
heapq.heapify(q)
result = 0
while q:
    cnt, check = heapq.heappop(q)
    a, b = check
    a = find_parent(a)
    b = find_parent(b)

    if a != b:
        result += cnt
        if a > b:
            parent[a] = b
        else :
            parent[b] = a
print(result)