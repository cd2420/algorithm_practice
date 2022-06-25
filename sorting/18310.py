# 안테나
n = int(input())
anthena = list(map(int, input().split()))
anthena.sort()
size = len(anthena)
if  size % 2 == 1:
    print(anthena[size // 2])
else :
    check = -1
    result = 0
    for i in [size // 2 - 1, size // 2]:
        tmp = 0
        for j in range(n):
            tmp += abs(anthena[j] - anthena[i])
        if check == -1:
            check = tmp
            result = i
        else :
            if check > tmp:
                check = tmp
                result = i
    print(anthena[result])