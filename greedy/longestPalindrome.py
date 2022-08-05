# 프로그래머스
# 가장 긴 팰린드롬
def solution(s):
    answer = 1
    for i in range(1, len(s)):
        left = i
        right = i
        while left-1 >= 0 and right + 1 < len(s) and s[left-1] == s[right+1]:
            left -= 1
            right += 1
        answer = max(answer, right - left + 1)
        left = i
        right = i
        check = 0
        while left - 1 >= 0 and right < len(s) and s[left-1] == s[right]:
            check += 2
            left -= 1
            right += 1
        answer = max(answer, check)
    return answer