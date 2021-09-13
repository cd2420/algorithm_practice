def back_tracking(n, m, cand):
    if len(cand) == m:
        result.append(cand[:])
        return
    for i in range(1, n + 1):
        if is_ok(i, cand):
            cand.append(i)
            back_tracking(n, m, cand)
            cand.pop()


def is_ok(data, cand):
    if data not in cand:
        return True
    else:
        return False


n, m = map(int, input().split())
result = []
back_tracking(n, m, [])
for r in result:
    for s in r:
        print(s, end=' ')
    print()
