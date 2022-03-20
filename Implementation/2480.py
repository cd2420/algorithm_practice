# 주사위 세개
dice = list(map(int, input().split()))
answer = 0
if len(set(dice)) == 1:
    answer = 10000 + dice[0] * 1000
elif len(set(dice)) == 2:
    temp_num = 0
    for i in dice:
        if temp_num != i:
            temp_num = i
        else:
            break
    answer = 1000 + temp_num * 100
else:
    answer = max(dice) * 100

print(answer)
