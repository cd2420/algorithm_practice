# 치킨 배달

def back_tracking(start, tmp):
    global result
    if len(tmp) == m:
        check = 0
        for h_x, h_y in home:
            check += getDist(h_x, h_y, tmp)
        result = min(result, check)
        return

    for idx in range(start, len(chicken)):
        i, j = chicken[idx]
        tmp.append((i, j))
        back_tracking(idx+1, tmp)
        tmp.pop()

def getDist(h_x, h_y, tmp):
    returnData = 1e9
    for c_x, c_y in tmp:
        returnData = min(returnData, abs(c_x - h_x) + abs(c_y - h_y))
    return returnData

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 1e9

home = []
chicken = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            home.append((x, y))
        if graph[x][y] == 2:
            chicken.append((x, y))

back_tracking(0, [])
print(result)