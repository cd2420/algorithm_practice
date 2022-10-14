# 프로그래머스
# 구명보트
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    l = 0
    r = len(people) - 1
    while l < r:
        sum = people[l] + people[r]
        l += 1
        if sum <= limit:
            r -= 1
        answer += 1
    if l == r :
        answer += 1
    return answer