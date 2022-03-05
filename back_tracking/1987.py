# 알파벳
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def back_tracking(x, y, tmp_str):
    global result
    q = set()
    q.add((x, y, tmp_str))
    while q:
        x, y, tmp_str = q.pop()
        result = max(result, len(tmp_str))
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] not in tmp_str:
                    q.add((nx, ny, tmp_str + graph[nx][ny]))


r, c = map(int, input().split())
graph = [input() for _ in range(r)]
result = 0
back_tracking(0, 0, graph[0][0])
print(result)
