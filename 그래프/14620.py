# 꽃길

directions = [(1,0), (-1,0), (0,-1), (0,1)]

def solve(x, y, z):
    global result
    tmp = set()
    cal_tmp(x, tmp)
    cal_tmp(y, tmp)
    cal_tmp(z, tmp)

    if len(tmp) != 15:
        return
    
    tmp_result = 0
    for tx, ty in tmp:
        tmp_result += arr[tx][ty]
    result = min(result, tmp_result)

def cal_tmp(x, tmp):
    x_r = x // N
    x_c = x % N
    tmp.add((x_r, x_c))
    for dx, dy in directions:
        nx = x_r + dx
        ny = x_c + dy
        if 0 <= nx < N and 0 <= ny < N:
            tmp.add((nx, ny))
    


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
check = N * N
result = 1e9
for i in range(check):
    for j in range(check):
        for k in range(check):
            solve(i, j, k)
print(result)