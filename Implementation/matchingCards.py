# 프로그래머스
# 카드 짝 맞추기
from itertools import permutations
from collections import deque, defaultdict
from copy import deepcopy


board = []
def ctrl_move(r, c, k, t):
    global board
    cr, cc = r, c
    while True:
        nr = cr + k
        nc = cc + t
        if not (0<=nr<4 and 0<=nc<4):
            return cr, cc
        if board[nr][nc] != 0:
            return nr, nc
        cr = nr
        cc = nc

def bfs(s_x, s_y, t_x, t_e):
    q = deque()
    q.append((s_x, s_y, 0))
    visited = [[False] * 4 for _ in range(4)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        x, y, cnt = q.popleft()
        if x == t_x and y == t_e:
            return cnt
        if visited[x][y]:
            continue
        visited[x][y] = True
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                q.append((nx, ny, cnt + 1))
            
            nx, ny = ctrl_move(x, y, dx, dy)
            q.append((nx, ny, cnt+1))
    return -1

def solution(input_board, r, c):
    global board
    board = input_board
    answer = 1e9
    dict_target = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                dict_target[board[i][j]].append((i, j))
    
    for lst in list(permutations(dict_target.keys())):
        now_x, now_y = r, c
        board = deepcopy(input_board)
        cnt = 0
        start = None
        end = None
        for target in lst:
            idx1, idx2 = dict_target[target]
            idx1_cnt = bfs(now_x, now_y, idx1[0], idx1[1])
            idx2_cnt = bfs(now_x, now_y, idx2[0], idx2[1])
            if idx2_cnt > idx1_cnt :
                start = idx1
                end = idx2
                cnt += idx1_cnt
            else :
                start = idx2
                end = idx1
                cnt += idx2_cnt

            cnt += bfs(start[0], start[1], end[0], end[1])
            cnt += 2
            board[start[0]][start[1]] = 0
            board[end[0]][end[1]] = 0
            now_x, now_y = end
        answer = min(answer, cnt)
    return answer