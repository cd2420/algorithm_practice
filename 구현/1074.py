def z(n, x, y):
    global result
    if n == 2:
        if x == r and y == c:
            print(result)
            return
        result += 1
        if x == r and y + 1 == c:
            print(result)
            return
        result += 1
        if x + 1 == r and y == c:
            print(result)
            return
        result += 1
        if x + 1 == r and y + 1 == c:
            print(result)
            return
        result += 1
        return

    z(n // 2, x, y)
    z(n // 2, x, y + n // 2)
    z(n // 2, x + n // 2, y)
    z(n // 2, x + n // 2, y + n // 2)


N, r, c = map(int, input().split())
result = 0
z(2 ** N, 0, 0)
