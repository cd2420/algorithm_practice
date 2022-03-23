# Maaaaaaaaaze
from collections import deque

def is_all_1(graph):
    cnt = 0
    for pan in graph:
        check_cnt = 0
        for check in pan:
            if len(list(set(check))) == 1 and list(set(check))[0] == 1:
                check_cnt += 1
        if check_cnt == 5:
            cnt += 1
    if cnt == 5:
        return True
    else :
        return False


def rotation(arr):
    n = 5
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = arr[i][j]
    return result

def copyarr(arr):
    tmp_arr = []
    for i in range(5):
        tmp_arr.append(arr[i][:])
    return tmp_arr

def make_maze(maze_idx, maze):
    if len(maze_idx) >= 5:
        # 2. 3차원 배열에서 미로찾기
        find_maze(maze)
        return
    
    for i in range(5):
        if i not in maze_idx:
            maze_idx.append(i)
            tmp_maze_i = copyarr(graph[i])
            for _ in range(4):
                maze.append(rotation(tmp_maze_i))
                make_maze(maze_idx, maze)
                tmp_maze_i = maze.pop()
            maze_idx.pop()


def find_maze(maze):
    # 2-1. 입구, 출구 꼭짓점 찾기
    for i in range(4):
        s_x, s_y, s_z = end_point[i]
        e_x, e_y, e_z = end_point[7 - i]
        if maze[s_x][s_y][s_z] == 1 and maze[e_x][e_y][e_z] == 1:
            bfs(maze, (s_x, s_y, s_z), (e_x, e_y, e_z))

def bfs(maze, start, end):
    global result
    q = deque([start])
    tmp_maze = [[[-1] * 5 for _ in range(5)] for __ in range(5)]
    tmp_maze[start[0]][start[1]][start[2]] = 1
    while q:
        x, y, z = q.popleft()
        if x == end[0] and y == end[1] and z == end[2]:
            result = min(result, tmp_maze[x][y][z])
            continue
        for dx, dy, dz in directions:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 and maze[nx][ny][nz] == 1:
                if tmp_maze[nx][ny][nz] == -1 or tmp_maze[nx][ny][nz] > tmp_maze[x][y][z] + 1:
                    tmp_maze[nx][ny][nz] = tmp_maze[x][y][z] + 1
                    q.append((nx, ny, nz))

end_point = [(0, 0, 0), (0, 0, 4), (0, 4, 0), (0, 4, 4)
            , (4, 0, 0), (4, 0, 4), (4, 4, 0), (4, 4, 4)]
directions = [(0,0,1), (0,1,0), (0,0,-1), (0,-1,0), (1,0,0), (-1, 0, 0)]
pan1 = [list(map(int, input().split())) for _ in range(5)]
pan2 = [list(map(int, input().split())) for _ in range(5)]
pan3 = [list(map(int, input().split())) for _ in range(5)]
pan4 = [list(map(int, input().split())) for _ in range(5)]
pan5 = [list(map(int, input().split())) for _ in range(5)]
graph = [pan1, pan2, pan3, pan4, pan5]
result = 1e9
if is_all_1(graph):
    print(12)
else :
    # 1. 큐브를 쌓는 순서
    # 1-1. 큐브를 회전
    make_maze([], [])
    print(result - 1 if result != 1e9 else -1)
