# 주식 가격
def solution(prices):
    answer = []
    for i in range(len(prices)):
        check = prices[i]
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if check > prices[j]:
                break
        answer.append(count)
    return answer
