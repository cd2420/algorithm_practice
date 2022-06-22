# 감시 피하기
from collections import deque
import sys

def is_pass(a, b, c):
    a_x, a_y = a // n, a % n 
    b_x, b_y = b // n, b % n
    c_x, c_y = c // n, c % n
    if a == 3 and b == 6 and c ==12 :
        1
    if arr[a_x][a_y] != 'X' or arr[b_x][b_y] != 'X' or arr[c_x][c_y] != 'X':
        return False
    check = set()
    check.add((a_x, a_y))
    check.add((b_x, b_y))
    check.add((c_x, c_y ))
    for t_x, t_y in teachers:
        for dx, dy in directions:
            if dfs(t_x, t_y, dx, dy, check):
                return False
            else:
                continue
    return True

def dfs(t_x, t_y, dx, dy, check):
    nx = t_x + dx
    ny = t_y + dy
    if (nx, ny) in check:
        return False
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        return False
    if arr[nx][ny] == "S":
        return True
    else :
        return dfs(nx, ny, dx, dy, check)

        
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n = int(input())
arr = [list(input().split()) for _ in range(n)]
teachers = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':
            teachers.append((i, j))

for i in range(n*n):
    for j in range(i+1, n*n):
        for k in range(j+1, n*n):
            if is_pass(i, j, k):
                print("YES")
                sys.exit(0)
print("NO")