# 튜플
def solution(s):
    answer = []
    s = s[2:-2]
    s_list = s.split("},{")
    s_list.sort(key=lambda x: len(x))
    for i in s_list:
        for j in i.split(","):
            if j not in answer:
                answer.append(j)
    answer = list(map(int, answer))
    return answer
