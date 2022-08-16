# 프로그래머스
# 외벽점검
from itertools import permutations
def solution(n, weak, dist):
    answer = len(dist) + 1
    check_weak = len(weak)
    weak.extend([w + n for w in weak])
    for w in range(check_weak):
        for friends in list(permutations(dist)):
            tmp_w = w
            now = weak[tmp_w] + friends[0]
            cnt = 1
            for index in range(w, w+check_weak):
                if now < weak[index]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    now = weak[index] + friends[cnt-1]
            answer = min(answer, cnt)
            
    return answer if answer <= len(dist) else -1