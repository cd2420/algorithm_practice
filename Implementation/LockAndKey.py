# 프로그래머스
# 자물쇠와 열쇠

def rotation90(arr):
    x = len(arr)
    tmp_arr = [[0] * x for _ in range(x)]
    for i in range(x):
        for j in range(len(arr[i])):
            tmp_arr[j][x - i - 1] = arr[i][j]
    return tmp_arr

def move(move_x, move_y, lock, key, lock_N):

    for i in range(len(key)):
        for j in  range(len(key[i])):
            lock[move_x+i][move_y+j] += key[i][j]
    tmp_check_lock = lock[lock_N: 2 * lock_N]
    check_lock = []
    for tmp in tmp_check_lock:
        check_lock.append(tmp[lock_N: 2 * lock_N])
    for check in check_lock:
        for c in check:
            if c != 1:
                for i in range(len(key)):
                    for j in  range(len(key[i])):
                        lock[move_x+i][move_y+j] -= key[i][j]
                return False
    return True
    
M = int(input())
key = [list(map(int, input().split())) for _ in range(M)]
N = int(input())
lock = [list(map(int, input().split())) for _ in range(N)]
tmp_N = len(lock) * 3
tmp_arr = [[0] * tmp_N for _ in range(tmp_N)]
for i in range(N):
    for j in range(N):
        tmp_arr[N+i][N+j] = lock[i][j]

for _ in range(4):
    key = rotation90(key)
    for move_num_i in range(tmp_N - M + 1):
        for move_num_j in range(tmp_N - M + 1):
            if move(move_num_i, move_num_j, tmp_arr, key, N):
                print(True)
print(False)
    # result_idx = N, N*2