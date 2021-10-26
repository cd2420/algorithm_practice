# 피로도
def is_ok(k, dungeon, tmp_finished):

    if (dungeon in tmp_finished) or (dungeon[1][0] > k):
        return False
    else:
        return True


def back_tarcking(k, tmp_dungeons, tmp_finished, length, result):

    if length == len(tmp_finished):
        result.add(len(tmp_finished))
        return

    for dungeon in tmp_dungeons:
        if is_ok(k, dungeon, tmp_finished):
            tmp_finished.append(dungeon)
            k -= dungeon[1][1]
            back_tarcking(k, tmp_dungeons, tmp_finished, length, result)
            k += dungeon[1][1]
            tmp_finished.pop()
        else:
            continue
    result.add(len(tmp_finished))


def solution(k, dungeons):
    answer = -1
    length = len(dungeons)
    tmp_dungeons = [[idx, dungeon] for idx, dungeon in enumerate(dungeons)]
    result = set()
    back_tarcking(k, tmp_dungeons, [], length, result)
    answer = max(result)
    return answer
