# 프로그래머스
# 광고삽입
def make_sec(time):
    s_h, s_m, s_s = map(int, time.split(":"))
    return s_h * 3600 + s_m * 60 + s_s

def make_str(time):
    
    s_h = str(time // 3600)
    s_h = s_h if len(s_h) > 1 else '0'+s_h
    time = time % 3600
    s_m = str(time // 60)
    s_m = s_m if len(s_m) > 1 else '0'+s_m
    time = time % 60
    s_s = str(time) if time >= 10 else '0'+str(time)
    return s_h + ":" + s_m + ":" + s_s

def solution(play_time, adv_time, logs):
    answer = 0
    totalSec = make_sec(play_time)
    dp = [0] * (totalSec + 1)
    advTimeSec = make_sec(adv_time)
    
    if totalSec == advTimeSec:
        return "00:00:00"
    
    for log in logs:
        startLog, endLog = log.split("-")
        startSec = make_sec(startLog)
        endSec = make_sec(endLog)
        dp[startSec] += 1
        dp[endSec] -= 1
    
    for i in range(1, len(dp)):
        dp[i] += dp[i-1]
    for i in range(1, len(dp)):
        dp[i] += dp[i-1]
    
    check = -1
    for i in range(advTimeSec, len(dp)):
        if i <= advTimeSec:
            check = dp[advTimeSec] - dp[i-advTimeSec]
        else :
            if check < dp[i] - dp[i-advTimeSec]:
                check = dp[i] - dp[i-advTimeSec]
                answer = i - advTimeSec + 1
    
    return make_str(answer)