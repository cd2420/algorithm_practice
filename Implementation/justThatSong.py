# 방금 그 곡
from collections import deque


def word_to_list(word, lst):
    for i in list(word):
        if i != '#':
            lst.append(i)
        else:
            lst.append(lst.pop() + '#')


def music_time(start, end):
    start_h, start_m = start.split(":")
    int_start = int(start_h) * 60 + int(start_m)
    end_h, end_m = end.split(":")
    int_end = int(end_h) * 60 + int(end_m)
    return int_end - int_start


def solution(m, musicinfos):
    answer = ''

    m_list = []
    word_to_list(m, m_list)
    result = []
    for i, musicinfo in enumerate(musicinfos):
        start, end, music, info = musicinfo.split(",")
        time = music_time(start, end)
        info_list = []
        word_to_list(info, info_list)

        play_info = []
        for t in range(time):
            info_idx = t % len(info_list)
            play_info.append(info_list[info_idx])

        q = deque(play_info)
        count = 0
        while q:
            if count == len(m_list):
                break
            x = q.popleft()
            for i in m_list:
                if x == i:
                    count += 1
                    if q:
                        x = q.popleft()
                    else:
                        break
                else:
                    if count > 0:
                        q.appendleft(x)
                    count = 0
                    break

        if count == len(m_list):
            result.append((time, i, music))
    if len(result) == 0:
        return '(None)'
    else:
        result.sort(key=lambda x: (-x[0], x[1]))
        answer = result[0][2]
    return answer
