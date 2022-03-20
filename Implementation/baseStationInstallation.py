# 기지국 설치
def solution(n, stations, w):
    answer = 0
    check = []
    if len(stations) == 1:
        if stations[0] == 1 or stations[0] == n:
            check.append(n - 1 - w)
        else:
            if stations[0] - w - 1 > 0:
                check.append(stations[0] - w - 1)
            if n - (stations[0] + w) > 0:
                check.append(n - (stations[0] + w))

    else:
        for i in range(len(stations)):
            if i == 0:
                if stations[i] == 1:
                    if (stations[i+1] - w) - (stations[i] + w) - 1 > 0:
                        check.append(
                            (stations[i+1] - w) - (stations[i] + w) - 1)
                else:
                    if stations[i] - w - 1 > 0:
                        check.append(stations[i] - w - 1)
                    if (stations[i+1] - w) - (stations[i] + w) - 1 > 0:
                        check.append(
                            (stations[i+1] - w) - (stations[i] + w) - 1)

            elif i == len(stations) - 1:
                if stations[i] != n:
                    if n - (stations[i] + w) > 0:
                        check.append(n - (stations[i] + w))

            else:
                if (stations[i+1] - w) - (stations[i] + w) - 1 > 0:
                    check.append((stations[i+1] - w) - (stations[i] + w) - 1)

    for c in check:
        answer += c // (2 * w + 1)
        if c % (2 * w + 1) > 0:
            answer += 1
    return answer
