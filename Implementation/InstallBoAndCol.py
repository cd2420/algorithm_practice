# 프로그래머스
# 기둥과 보 설치
arr_0 = set() # 기둥 좌표 모음
arr_1 = set() # 보 좌표 모

def impl(x, y, a, b):
    if b == 0 :
        if a == 1 :
            arr_1.discard((x, y))
        else:
            arr_0.discard((x, y))
        
        if not is_ok_check():
            if a == 1:
                arr_1.add((x, y))
            else :
                arr_0.add((x, y))
    else :
        if a == 1:
            arr_1.add((x, y))
        else :
            arr_0.add((x, y))
            
        if not is_ok_check():
            if a == 1:
                arr_1.discard((x, y))
            else :
                arr_0.discard((x, y))
    
def is_ok_check():
    for x, y in arr_0:
        if y != 0 and (x, y-1) not in arr_0:
            if (x, y) not in arr_1 and (x-1, y) not in arr_1:
                return False
    for x, y in arr_1:
        if (x, y-1) not in arr_0 and (x+1, y-1) not in arr_0:
            if (x+1, y) not in arr_1 or (x-1, y) not in arr_1:
                return False
    return True
                
    
def solution(n, build_frame):
    answer = []
    # x, y = 좌표
    # a = 구조물 종류, 0: 기둥, 1: 보
    # b = 설치 유무, 0: 삭제, 1: 설치
    for x, y, a, b in build_frame:
        impl(x, y, a, b)
    for x, y in arr_0:
        answer.append([x,y,0])
    for x, y in arr_1:
        answer.append([x,y,1])
    answer.sort()
    return answer