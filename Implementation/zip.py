# 압축
def solution(msg):
    answer = []
    word = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    tmp_word = ''

    msg_idx = 0
    while msg_idx < len(msg):
        tmp_word += msg[msg_idx]

        if tmp_word in word:
            result = word.index(tmp_word)
            if msg_idx == len(msg) - 1:
                answer.append(result)
            msg_idx += 1
        else:
            word.append(tmp_word)
            answer.append(word.index(tmp_word[:-1]))
            tmp_word = ''

    return answer
