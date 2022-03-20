# 새로운 게임
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[] for __ in range(n)] for _ in range(n)]
direction = {
    1: (0, 1),
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0),
}
horses = [list(map(int, input().split())) for _ in range(k)]
for i in range(len(horses)):
    x, y = horses[i][0] - 1, horses[i][1] - 1
    dp[x][y].append(i)

count = 1
while count <= 1000:

    idx = 0
    blue_count = 0
    is_finish = False
    while idx < len(horses):
        x, y, dir = horses[idx][0] - 1, horses[idx][1] - 1, horses[idx][2]
        if idx not in dp[x][y]:
            idx += 1
            continue
        else:
            if dp[x][y].index(idx) > 0:
                idx += 1
                continue

            dx, dy = direction[dir]
            nx = x + dx
            ny = y + dy
            # 말판을 벗어날려는 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                if blue_count == 0:
                    if dir % 2 == 1:
                        dir += 1
                    else:
                        dir -= 1
                    horses[idx][2] = dir
                    blue_count += 1
                else:
                    blue_count = 0
                    idx += 1
                continue

            # 1. 흰색 인 경우
            if graph[nx][ny] == 0:
                while dp[x][y]:
                    horse = dp[x][y].pop(0)
                    horses[horse][0], horses[horse][1] = nx + 1, ny + 1
                    dp[nx][ny].append(horse)
                blue_count = 0
                idx += 1
            # 2. 빨간색인 경우
            elif graph[nx][ny] == 1:
                while dp[x][y]:
                    horse = dp[x][y].pop()
                    horses[horse][0], horses[horse][1] = nx + 1, ny + 1
                    dp[nx][ny].append(horse)
                blue_count = 0
                idx += 1
            # 3. 파란색인 경우
            else:
                if blue_count == 0:
                    if dir % 2 == 1:
                        dir += 1
                    else:
                        dir -= 1
                    horses[idx][2] = dir
                    blue_count += 1
                else:
                    blue_count = 0
                    idx += 1
            if len(dp[nx][ny]) >= 4:
                is_finish = True
                break
    if is_finish:
        break
    else:
        count += 1
if count > 1000:
    print(-1)
else:
    print(count)
