# 프로그래머스
# 스타 수열
from collections import Counter
def solution(a):
    
    answer = 0
    counter = Counter(a)
    
    for k in counter.keys():
        
        if counter[k] <= answer:
            continue
        target = k
        idx = 0
        tmp = 0
        while idx < len(a)-1:
            now = a[idx]
            if now != target:
                if a[idx+1] == target:
                    tmp += 1
                    idx += 2
                else:
                    idx += 1
            else:
                if a[idx+1] != target:
                    tmp += 1
                    idx += 2
                else:
                    idx += 1
        answer = max(tmp, answer)
    return answer * 2 if answer != 0 else 0
solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0])