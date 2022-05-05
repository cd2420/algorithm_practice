# 택배
N, C = map(int, input().split())
M = int(input())
check = [list(map(int, input().split())) for _ in range(M)]
check.sort(key=lambda x:x[1])
step_volume = [C] * (N+1)
result = 0
for c in check:
    start, end, vol = c
    tmp = 1e9
    for i in range(start, end):
        s_v = step_volume[i]
        if s_v >= vol :
            tmp = min(tmp, vol)
        else :
            tmp = min(tmp, s_v)

    for i in range(start, end):
        step_volume[i] -= tmp
    result += tmp
print(result)
