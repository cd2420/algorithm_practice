# 프로그래머스
# 블록 이동하기
from collections import deque

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution(board):
    answer = 1e9
    n = len(board)
    visited = list()
    start = set()
    start.add((0, 0))
    start.add((0, 1))
    visited.append(start)
    q = deque([])
    q.append((start, 0))
    while q :
        now , cnt = q.popleft()
        a,b = now
        ax, ay = a
        bx, by = b
        if (ax == n-1 and ay == n-1) or (bx == n -1 and by == n-1):
            answer = min(answer, cnt)
            break

        for dx, dy in directions:
            nax = ax + dx
            nay = ay + dy
            nbx = bx + dx
            nby = by + dy
            
            if 0 <= nax < n and 0 <= nay < n and 0 <= nbx < n and 0 <= nby < n:
                if board[nax][nay] or board[nbx][nby]:
                    continue
                tmp = set()
                tmp.add((nax, nay))
                tmp.add((nbx, nby))
                if tmp in visited:
                    continue
                visited.append(tmp)
                q.append((tmp, cnt + 1))
                
        if ax - bx == 0:
            for dx, dy in [(1, 0), (-1, 0)]:
                nax = ax + dx
                nay = ay + dy

                if 0 <= nax < n and 0 <= nay < n and board[nax][nay] != 1:
                    nbx = bx + dx
                    nby = by + dy
                    if 0 <= nbx < n and 0 <= nby < n and board[nbx][nby] != 1:
                        tmp = set()
                        tmp.add((bx, by))
                        tmp.add((nbx, nby))
                        if tmp in visited:
                            continue
                        visited.append(tmp)
                        q.append((tmp, cnt + 1))

                nbx = bx + dx
                nby = by + dy
                if 0 <= nbx < n and 0 <= nby < n and board[nbx][nby] != 1:
                    nax = ax + dx
                    nay = ay + dy
                    if 0 <= nax < n and 0 <= nay < n and board[nax][nay] != 1:
                        tmp = set()
                        tmp.add((ax, ay))
                        tmp.add((nax, nay))
                        if tmp in visited:
                            continue
                        visited.append(tmp)
                        q.append((tmp, cnt + 1))
        else :
            for dx, dy in [(0, 1), (0, -1)]:
                nax = ax + dx
                nay = ay + dy

                if 0 <= nax < n and 0 <= nay < n and board[nax][nay] != 1:
                    nbx = bx + dx
                    nby = by + dy
                    if 0 <= nbx < n and 0 <= nby < n and board[nbx][nby] != 1:
                        tmp = set()
                        tmp.add((bx, by))
                        tmp.add((nbx, nby))
                        if tmp in visited:
                            continue
                        visited.append(tmp)
                        q.append((tmp, cnt + 1))

                nbx = bx + dx
                nby = by + dy
                if 0 <= nbx < n and 0 <= nby < n and board[nbx][nby] != 1:
                    nax = ax + dx
                    nay = ay + dy
                    if 0 <= nax < n and 0 <= nay < n and board[nax][nay] != 1:
                        tmp = set()
                        tmp.add((ax, ay))
                        tmp.add((nax, nay))
                        if tmp in visited:
                            continue
                        visited.append(tmp)
                        q.append((tmp, cnt + 1))
    return answer