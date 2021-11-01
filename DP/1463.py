# 1로 만들기
x = int(input())
if x == 1:
    print(0)
else:
    a = set()
    a.add(x)
    dp = [a]
    count = 0
    while dp:
        tmp = set()
        count += 1
        for i in dp.pop():
            if i % 3 == 0:
                tmp.add(i // 3)
            if i % 2 == 0:
                tmp.add(i // 2)
            if i - 1 >= 1:
                tmp.add(i - 1)
        if 1 in tmp:
            break
        else:
            dp.append(tmp)
    print(count)
