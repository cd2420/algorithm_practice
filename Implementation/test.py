directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def rotated(a):
    n = len(a)
    m = len(a[0])

    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def dfs(num, dir, check, x, y, graph, clockwise, n):
    
    graph[x][y] = num
    dx, dy = directions[dir]
    if dir % 2 == 0 and not clockwise:
        dy *= -1
    nx = x + dx
    ny = y + dy
    if 0 <= nx < n and 0 <= ny < n:
        if nx == n - check - 1 or nx == check or ny == n - check - 1 or ny == check:
            dir = (dir + 1) % 4
            check += 1
        dfs(num + 1, dir, check, nx, ny, graph, clockwise, n)


n = int(input())
clockwise = bool(input())
graph = [[0] * n for _ in range(n)]

start_x, start_y = 0, 0
if not clockwise: 
    start_x, start_y = 0, n-1
dfs(1, 0, 1, start_x, start_y, graph, clockwise, n)


for g in graph:
    print(g)