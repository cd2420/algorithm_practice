# 문자열 판별
# 재귀함수 사용이 편할 경우:
# 1. 연속으로 체크할 경우 문제가 발생할때
# 2. 다음 상황에서 여러 가지 경우를 고려해야 할 경우(Ex. 백트래킹)

def sol(idx):
    global result
    if idx == len(s):
        result = 1
        return
    if dp[idx]:
        return
    dp[idx] = 1
    for word in words:
        size = len(word)
        if size + idx > len(s):
            continue
        if word == s[idx:idx+size]:
            sol(idx+size)

s = input()
n = int(input())
words = [input() for _ in range(n)]
result = 0
dp = [0] * 101
sol(0)
print(result)