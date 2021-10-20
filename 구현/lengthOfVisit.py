# 방문 길이
def solution(dirs):
    answer = 0
    start = (0, 0)
    result = set()
    check = {
        'U': [0, 1], 'L': [-1, 0], 'R': [1, 0], 'D': [0, -1]
    }

    for _dir in dirs:
        x, y = start
        dx, dy = check[_dir]
        nx = x + dx
        ny = y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (x, y, nx, ny) not in result and (nx, ny, x, y) not in result:
                result.add((x, y, nx, ny))
                result.add((nx, ny, x, y))
                answer += 1
            start = (nx, ny)

    return answer
