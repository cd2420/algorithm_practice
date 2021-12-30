# 늑대의 왕

def check():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'W':
                for dx, dy in directions:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < r and 0 <= ny < c:
                        if graph[nx][ny] == 'S':
                            print(0)
                            return False
                        elif graph[nx][ny] == '.':
                            graph[nx][ny] = 'D'
    return True


r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
if(check()):
    print(1)
    for g in graph:
        print(''.join(g))
