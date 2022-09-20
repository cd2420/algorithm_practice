# 미네랄 2
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


def fall():
    will_fall = []
    for y in range(r - 1):
        for x in range(c):
            if visited[y][x] == 0 and board[y][x] == 'x':
                will_fall.append((y, x))
    if len(will_fall) == 0:
        return
    degree = 1
    for y, x in will_fall:
        board[y][x] = '.'
    while True:
        can_go = True
        for y, x in will_fall:
            if y + degree >= r or board[y + degree][x] == 'x':
                can_go = False
                break
        if can_go is False:
            break
        degree += 1
    degree -= 1
    for y, x in will_fall:
        board[y + degree][x] = 'x'



def dfs(y, x):
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < r and 0 <= nx < c and visited[ny][nx] == 0 and board[ny][nx] == 'x':
            visited[ny][nx] = 1
            dfs(ny, nx)


def throw(y, d):
    if d == 0:
        x = 0
        while x < c and board[y][x] == '.':
            x += 1
        if x < c:
            board[y][x] = '.'
    else:
        x = c - 1
        while x >= 0 and board[y][x] == '.':
            x -= 1
        if x >= 0:
            board[y][x] = '.'


r, c = map(int, input().strip().split())
board = [list(input()) for _ in range(r)]

n = int(input())
heights = list(map(int, input().strip().split()))
for i, height in enumerate(heights):
    y = r - height
    d = i % 2
    throw(y, d)
    visited = [[0 for _ in range(c)] for _ in range(r)]

    for x in range(c):
        if board[r-1][x] == 'x':
            visited[r-1][x] = 1
            dfs(r-1, x)
    fall()


for y in range(r):
    print(''.join(board[y]))