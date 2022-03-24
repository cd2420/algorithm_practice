# 스티커 붙이기
from collections import deque

def rotation(arr):
    n = len(arr)
    m = len(arr[0])
    tmp_return = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            tmp_return[j][n-i-1] = arr[i][j]
    return tmp_return

def put_sticker(cnt, sticker):
    # 4. 270도 까지 회전 후 붙일수 없다면 버림
    if cnt >= 4:
        return
    # 2 스티커를 한칸씩 이동시키면서 겹치지 않는 부분 확인
    is_ok = False
    for x in range(N):
        for y in range(M):
            if check(x, y, sticker):
                is_ok = True
                break
        if is_ok:
            break

    # 3. 불가능 하다면 90도 회전
    if not is_ok:
        put_sticker(cnt + 1, rotation(sticker))
    
def check(x, y, sticker):
    tmp_idx = []
    for dx in range(len(sticker)):
        nx = x + dx
        if 0 <= nx < N:
            for dy in range(len(sticker[0])):
                ny = y + dy
                if 0 <= ny < M:
                    if graph[nx][ny] + sticker[dx][dy] <= 1 :
                        tmp_idx.append((nx, ny, graph[nx][ny] + sticker[dx][dy]))
                    else :
                        return False
                else :
                    return False
        else :
            return False
    for x, y, val in tmp_idx:
        graph[x][y] = val
    return True


N, M, K = map(int, input().split())
stickers = deque([])
for _ in range(K):
    R, C = map(int, input().split())
    stickers.append([list(map(int, input().split())) for _ in range(R)])

# 0. 격자무늬 코드
graph = [[0] * M for _ in range(N)]
# 1. 먼저 받은 스티커부터 차례대로 격자에 맞춰서 붙임
while stickers:
    sticker = stickers.popleft()
    # 1-1. 회전 시키지 않고 붙임
    # 1-2. 붙이는 코드
    put_sticker(0, sticker)
result = N * M
for g in graph:
    zero = g.count(0)
    result -= zero
print(result)