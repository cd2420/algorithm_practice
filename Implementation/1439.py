# 뒤집기
S = input()
if S[0] == '1':
    check_0 = 0
    check = '1'
    for i in range(1, len(S)):
        if S[i] != check:
            check = S[i]
            if check == '0':
                check_0 += 1
    print(check_0)
else :
    check_1 = 0
    check = '0'
    for i in range(1, len(S)):
        if S[i] != check:
            check = S[i]
            if check == '1':
                check_1 += 1
    print(check_1)