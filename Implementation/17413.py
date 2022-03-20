# 단어 뒤집기 2
s = input()
s_lst = list(s)
result = ''
tmp_word = []
while s_lst:
    x = s_lst.pop(0)
    if x == '<':
        if tmp_word:
            result += ''.join(tmp_word)
            tmp_word = []
        while x != '>':
            result += x
            x = s_lst.pop(0)
        result += x
    elif x != ' ':
        tmp_word.insert(0, x)
    else:
        result += ''.join(tmp_word) + ' '
        tmp_word = []
if tmp_word:
    result += ''.join(tmp_word)
print(result)
