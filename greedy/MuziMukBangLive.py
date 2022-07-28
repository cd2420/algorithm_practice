# 프로그래머스
# 무지의 먹방 라이브
def solution(food_times, k):
    answer = 0
    food_times = [(food_times[i], i+1) for i in range(len(food_times))]
    food_times.sort(reverse=True)
    n = len(food_times)
    prev = 0
    while food_times and (food_times[-1][0] - prev) * n <= k:
        target = food_times.pop()
        k -= (target[0] - prev) * n
        prev = target[0]
        n = len(food_times)
    food_times.sort(key=lambda x:x[1])
    n = len(food_times)
    if n == 0:
        return -1
    k = k % n
    answer = food_times[k][1]
    return answer