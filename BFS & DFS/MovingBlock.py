# 프로그래머스
# 블록 이동하기
from collections import deque

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution(board):
    answer = 0
    n = len(board)
    check_cnt =[[0] * n for _ in range(n)]
    visited = list()
    start = set()
    start.add((0, 0))
    start.add((0, 1))
    visited.append(start)
    q = deque([])
    q.append(start)
    while q :
        a, b = q.popleft()
        ax, ay = a
        bx, by = b
        if (ax == n-1 and ay == n-1) or (bx == n -1 and by == n-1):
            answer = check_cnt[n-1][n-1]
            break
        cnt = min(check_cnt[ax][ay], check_cnt[bx][by])
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
                check_cnt[nax][nay] = cnt + 1
                check_cnt[nbx][nby] = cnt + 1
                visited.append(tmp)
                q.append(tmp)
                
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
                        check_cnt[bx][by] = cnt + 1
                        check_cnt[nbx][nby] = cnt + 1
                        visited.append(tmp)
                        q.append(tmp)

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
                        check_cnt[ax][ay] = cnt + 1
                        check_cnt[nax][nay] = cnt + 1
                        visited.append(tmp)
                        q.append(tmp)
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
                        check_cnt[bx][by] = cnt + 1
                        check_cnt[nbx][nby] = cnt + 1
                        visited.append(tmp)
                        q.append(tmp)

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
                        check_cnt[ax][ay] = cnt + 1
                        check_cnt[nax][nay] = cnt + 1
                        visited.append(tmp)
                        q.append(tmp)
    for c in check_cnt:
        print(c)
                
    return answer
solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])