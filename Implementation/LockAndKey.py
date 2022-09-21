# 프로그래머스
# 자물쇠와 열쇠

def rotation(arr):
    n = len(arr)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = arr[i][j]
    return result

def find_key(key, graph, lock_len):
    m = len(key)
    n = len(graph)
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            move_key(key, graph, i, j)
            if check(graph, lock_len):
                return True
            for x in range(m):
                for y in range(m):
                    graph[i+x][j+y] -= key[x][y]
    return False
                
            
def move_key(key, graph, x, y):
    m = len(key)
    for i in range(m):
        for j in range(m):
            graph[i+x][j+y] += key[i][j]
            
def check(graph, n):
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            if graph[i][j] != 1:
                return False
    return True
    
    

def solution(key, lock):
    n = len(lock)
    graph = [[0] * 3 * n for _ in range(3 * n)]
    for i in range(n):
        for j in range(n):
            graph[i+n][j+n] = lock[i][j]

    for _ in range(4):
        key = rotation(key)
        if find_key(key, graph, n):
            return True
    return False