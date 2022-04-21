# 행렬

def check(x, y):
    if 0 <= x + 2 < N and 0 <= y + 2 < M:
        for xx in range(3):
            for yy in range(3):
                A[x + xx][y + yy] = (A[x + xx][y + yy] + 1) % 2
        return True
    else :
        return False

def same():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    return True

N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            if check(i, j):
                result += 1
if same():
    print(result)
else :
    print(-1)
















