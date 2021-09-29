# 경주로 건설
from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(board, x, y, direction):

    visited = [[0] * len(board) for _ in range(len(board))]
    visited[x][y] = 1

    q = deque([])
    q.append([x, y, direction, 0])

    result = []

    while q:
        x, y, ex_direction, cost = q.popleft()

        if x == len(board) - 1 and y == len(board) - 1:
            result.append(cost)
            continue

        for direction in range(len(directions)):
            dx = directions[direction][0]
            dy = directions[direction][1]

            nx = x + dx
            ny = y + dy

            if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 0:

                new_cost = 0
                if ex_direction % 2 == direction % 2:
                    new_cost = cost + 100
                else:
                    new_cost = cost + 600

                if not visited[nx][ny] or visited[nx][ny] > new_cost:
                    visited[nx][ny] = new_cost
                    q.append([nx, ny, direction, new_cost])

    return min(result)


def solution(board):
    answer = 0

    min_1 = bfs(board, 0, 0, 1)
    min_2 = bfs(board, 0, 0, 0)

    answer = min(min_1, min_2)

    return answer
