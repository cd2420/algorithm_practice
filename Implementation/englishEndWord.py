# 프로그래머스
# 영어끝말잇기
def solution(n, words):
    count = 1
    left = []
    check = set()
    while words:
        for i in range(1, n+1):
            if words:
                word = words.pop(0)
                if left :
                    if left[-1][-1] == word[0]:
                        if word in check:
                            return [i, count]
                    else:
                        return [i, count]
                left.append(word)
                check.add(word)
            else :
                break
        count += 1
    return [0, 0]