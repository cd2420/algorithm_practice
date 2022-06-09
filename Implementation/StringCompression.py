# 프로그래머스
# 문자열 압축
s = input()
check = len(s)
result = 1e9
if len(s) == 1:
    print(1)
else:
    for size in range(1, check // 2 + 1):
        tmp_str = ''
        tmp_num = 1
        for i in range(0, check, size):
            if i + size >= check:
                if tmp_num <= 1:
                    tmp_str += s[i:i+size]
                else :
                    tmp_str += str(tmp_num) + s[i:i+size]
                break
            if s[i:i+size] == s[i+size: i+2*size]:
                tmp_num += 1
            else :
                if tmp_num <= 1:
                    tmp_str += s[i:i+size]
                else :
                    tmp_str += str(tmp_num) + s[i:i+size]
                tmp_num = 1
        result = min(result, len(tmp_str))
    print(result)