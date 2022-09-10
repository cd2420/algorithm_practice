# 프로그래머스
# 외벽점검
from itertools import permutations
def solution(n, weak, dist):
    answer = 1e9
    size = len(weak)
    check_size = len(dist)
    weak.sort()
    weak = weak + [w + n for w in weak]

    for i in range(size):
        for friends in permutations(dist):
            idx = 0
            start = weak[i] + friends[idx]
            for nxt in weak[i+1:i+size]:
                if start >= nxt:
                    continue
                else :
                    idx += 1
                    if idx >= len(friends):
                        break
                    start = nxt + friends[idx]
            else:
                answer = min(answer, idx+1)
            
    return answer if answer != 1e9 else -1