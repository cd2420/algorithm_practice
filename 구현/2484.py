# 주사위 네개
def getNum(dice):
    if len(set(dice)) == 1:
        return 50000 + dice[0] * 5000
    elif len(set(dice)) == 2:
        # 같은 눈이 2개씩 두 쌍인 경우
        if dice[1] != dice[2]:
            return 2000 + dice[1] * 500 + dice[2] * 500
        else:
            return 10000 + dice[1] * 1000
    elif len(set(dice)) == 3:
        temp_num = -1
        for i in dice:
            if temp_num != i:
                temp_num = i
            else:
                break
        return 1000 + temp_num * 100
    else:
        return max(dice) * 100


n = int(input())
result = -1
for i in range(n):
    dice = sorted(list(map(int, input().split())))
    result = max(result, getNum(dice))

print(result)
