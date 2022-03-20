# 추석 트래픽

def get_end_time(end_time):
    h = int(end_time[:2]) * 3600 * 1000
    m = int(end_time[3:5]) * 60 * 1000
    s = int(float(end_time[6:]) * 1000)
    return h + m + s


def get_start_time(end_time_sec, take_time):
    take_time_int = int(float(take_time[:-1]) * 1000)
    return end_time_sec - take_time_int + 1


def solution(lines):
    answer = 0
    for i in range(len(lines)):
        standard_s = lines[i].split()
        standard_end_time = standard_s[1]
        standard_end_time_sec = get_end_time(standard_end_time)
        count = 1
        for j in range(i+1, len(lines)):
            compare_s = lines[j].split()
            compare_end_time, compare_take_time = compare_s[1], compare_s[2]
            compare_end_time_sec = get_end_time(compare_end_time)
            compare_start_time_sec = get_start_time(
                compare_end_time_sec, compare_take_time)
            if standard_end_time_sec + 1000 > compare_start_time_sec and standard_end_time_sec <= compare_end_time_sec:
                count += 1
        answer = max(answer, count)
    return answer
