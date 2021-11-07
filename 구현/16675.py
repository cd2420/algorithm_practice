# 두 개의 손
def checkFightLose(a, person):
    if (a == 'R' and person['L'] == 'S') and (a == 'R' and person['R'] == 'S'):
        return True
    if (a == 'S' and person['L'] == 'P') and (a == 'S' and person['R'] == 'P'):
        return True
    if (a == 'P' and person['L'] == 'R') and (a == 'P' and person['R'] == 'R'):
        return True
    return False


def fight(MS, TK):
    is_MS_WIN = False
    is_TK_WIN = False
    for M in MS:
        if checkFightLose(MS[M], TK):
            is_MS_WIN = True
            break
    for T in TK:
        if checkFightLose(TK[T], MS):
            is_TK_WIN = True
            break
    if is_MS_WIN and is_TK_WIN:
        return '?'
    elif is_MS_WIN:
        return 'MS'
    elif is_TK_WIN:
        return 'TK'
    else:
        return '?'


M_L, M_R, T_L, T_R = input().split()
MS = {
    'L': M_L,
    'R': M_R
}
TK = {
    'L': T_L,
    'R': T_R
}
print(fight(MS, TK))
