# 어른 상어
from collections import deque

def check_available_dir(lst, i, shark_dir, tmp_loc):
    for dir in sharks_dir[i][shark_dir]:
        if dir in lst:
            dx, dy = directions[dir]
            nx = x + dx
            ny = y + dy
            sharks[i][0] = dir
            tmp_loc[nx][ny].append(i)
            tmp_loc[nx][ny].sort()
            return


N, M, k = map(int, input().split())
tmp_graph = [list(map(int, input().split())) for _ in range(N)]
# 1: 위
# 2: 아래
# 3: 왼쪽
# 4: 오른쪽
directions = {
    1: (-1, 0)
    , 2: (1, 0)
    , 3: (0, -1)
    , 4: (0, 1)
}

sharks = {}
for idx, val in enumerate(list(map(int, input().split()))):
    sharks[idx + 1] = [val, deque([])]

sharks_dir = {}
for i in range(1, M+1):
    sharks_dir[i] = {}
    for j in range(1, 5):
        sharks_dir[i][j] = list(map(int, input().split()))

graph = []
for i in range(N):
    tmp_lst = []
    for j in range(N):
        if tmp_graph[i][j] == 0 :
            tmp_lst.append([0, 0])
        else :
            tmp_lst.append([tmp_graph[i][j], k])
            sharks[tmp_graph[i][j]][1].append([i, j])
    graph.append(tmp_lst)

result = 0
while True:
    if result > 1000:
        result = -1
        break
    shark_num = 0
    tmp_loc = [[[] for __ in range(N)] for _ in range(N)]
    for i in range(1, M+1):
        shark_dir, loc = sharks[i]
        tmp_no_smell_dir = []
        tmp_my_smell_dir = []
        if not loc:
            continue
        else :
            shark_num += 1
            x,y = loc[-1]
            for dir in range(1,5):
                dx, dy = directions[dir]
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny][1] == 0:
                        tmp_no_smell_dir.append(dir)
                    elif graph[nx][ny][0] == i:
                        tmp_my_smell_dir.append(dir)
            if tmp_no_smell_dir:
                check_available_dir(tmp_no_smell_dir, i, shark_dir, tmp_loc)
            else :
                check_available_dir(tmp_my_smell_dir, i, shark_dir, tmp_loc)
    
    for i in range(N):
        for j in range(N):
            if graph[i][j][1] > 0:
                graph[i][j][1] -= 1
                if graph[i][j][1] == 0:
                    graph[i][j][0] = 0
            if tmp_loc[i][j]:
                idx = tmp_loc[i][j].pop(0)
                graph[i][j][0] = idx
                graph[i][j][1] = k
                sharks[idx][1] = deque([[i, j]])
                while tmp_loc[i][j]:
                    idx = tmp_loc[i][j].pop()
                    sharks[idx][1] = []
    if shark_num > 1:
        result += 1
    else :
        break
print(result)