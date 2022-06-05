# 만들 수 없는 금액
n = int(input())
money = list(map(int, input().split()))
money.sort()
result = 1
check = money[0]
if check > 1:
    print(1)
else:
    for i in range(1, n):
        m = money[i]
        if m > check + 1:
            break
        check += m
    print(check + 1)