# 프로그래머스
# 퍼즐 조각 채우기
from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def find(x, y, visited, graph, check):
    if visited[x][y]:
        return False
    if graph[x][y] == (check + 1) % 2:
        return False
    visited[x][y] = True
    result = [(x, y)]
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        
        for dx, dy in directions:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] ==  check and not visited[nx][ny]:
                    visited[nx][ny] = True
                    result.append((nx, ny))
                    q.append((nx, ny))
    return result


def init(graph):
    min_n = min(graph, key=lambda x:x[0])[0]
    min_m = min(graph, key=lambda x:x[1])[1]
    result = []
    for g in graph:
        result.append((g[0] - min_n, g[1] - min_m))
    return result

def rotate(graph):

    result = []
    min_n = min(graph, key=lambda x:x[0])[0]
    min_m = min(graph, key=lambda x:x[1])[1]
    max_n = max(graph, key=lambda x:x[0])[0]
    max_m = max(graph, key=lambda x:x[1])[1]
    check = max(max_n- min_n, max_m - min_m) + 1
    tmp_graph = [[0] * check for _ in range(check)]
    tmp_graph2 = [[0] * check for _ in range(check)]
    for x, y in graph:
        tmp_graph[x][y] = 1
        
    for i in range(check):
        for j in range(check):
            tmp_graph2[j][check - i - 1] = tmp_graph[i][j]
    for i in range(check):
        for j in range(check):
            if tmp_graph2[i][j] == 1:
                result.append((i, j))
    return result
            
def is_same(target, check):
    result = set(target)
    for c in check:
        result.add(c)
    return len(target) == len(result)

def solution(game_board, table):
    answer = 0
    targets = []
    n = len(game_board)
    m = len(game_board[0])
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            target = find(i, j, visited, game_board, 0)
            if target:
                targets.append(target)
    checks = []
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            tmp_check = find(i, j, visited, table, 1)
            if tmp_check:
                checks.append(tmp_check)
    targets = list(map(init, targets))
    checks = list(map(init, checks))
    
    for target in targets:
        is_exist = False
        for i in range(len(checks)):
            check = checks[i]
            if len(check) != len(target):
                continue
            for _ in range(4):
                check = init(rotate(check))
                if is_same(target, check):
                    answer += len(check)
                    is_exist = True
                    checks.pop(i)
                    break
            if is_exist:
                break
    return answer