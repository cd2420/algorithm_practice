# 프로그래머스
# 셔틀버스
def changeInt(timetable):
    result = []
    for t in timetable:
        h,m = map(int, t.split(":"))
        h *= 60
        result.append(h+m)
    return result

def changeStr(time):
    h = str(time // 60)
    m = str(time % 60)
    if len(h) == 1:
        h = "0" + h
    if len(m) == 1:
        m = "0" + m
    return h + ":" + m

def solution(n, t, m, timetable):
    answer = ''
    timetableToInt = changeInt(timetable)
    timetableToInt.sort(reverse=True)
    start = 540
    end = 1440
    
    while n != 1:
        cnt = 0
        while timetableToInt and start >= timetableToInt[-1]:
            timetableToInt.pop()
            cnt += 1
            if cnt == m:
                break
        start += t
        n -= 1
    
    while timetableToInt and start >= timetableToInt[-1]:
        time = timetableToInt.pop()
        if start >= time:
            m -=1
        if m == 0:
            return changeStr(time - 1)
        
    return changeStr(start)