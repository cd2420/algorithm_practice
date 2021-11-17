# 파이프 옮기기 1

# 0 : 가로, 1 : 세로, 2:대각선
def dfs(start):
    x, y, type = start
    if x == N-1 and y == N-1:
        return 1
    if dp[x][y][type] != -1:
        return dp[x][y][type]
    dp[x][y][type] = 0
    for dx, dy, n_type in type_dict[type]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if check_wall(nx, ny, n_type):
                dp[x][y][type] += dfs((nx, ny, n_type))
    return dp[x][y][type]


def check_wall(x, y, type):
    if type != 2 and graph[x][y] == 1:
        return False
    if type == 2:
        if graph[x][y] == 1 or graph[x-1][y] == 1 or graph[x][y-1] == 1:
            return False
    return True


type_dict = {
    0: [(0, 1, 0), (1, 1, 2)],
    1: [(1, 0, 1), (1, 1, 2)],
    2: [(1, 0, 1), (0, 1, 0), (1, 1, 2)]
}

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[[-1, -1, -1] for j in range(N)] for _ in range(N)]
dp[0][0] = [0, 0, 0]
print(dfs((0, 1, 0)))
