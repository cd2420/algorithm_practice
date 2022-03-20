# 쿼드압축후 개수세기
def arr_all_same(start_n, start_m, n, arr, total_len):
    check_num = arr[start_n][start_m]
    for i in range(start_n, start_n + n):
        tmp_arr = arr[i][start_m:start_m+n]
        if len(set(tmp_arr)) > 1:
            return False
        else:
            if check_num != tmp_arr[0]:
                return False
    return True


def make_zip(start_n, start_m, n, arr, total_len, result_dict):

    if n == 2:
        if arr_all_same(start_n, start_m, n, arr, total_len):
            check_num = arr[start_n][start_m]
            result_dict[check_num] += 1
        else:
            for i in [(0, 0), (0, 1), (1, 0), (1, 1)]:
                check_num = arr[start_n + i[0]][start_m + i[1]]
                result_dict[check_num] += 1
        return
    else:
        if arr_all_same(start_n, start_m, n, arr, total_len):
            check_num = arr[start_n][start_m]
            result_dict[check_num] += 1
        else:
            make_zip(start_n, start_m, n // 2, arr, total_len, result_dict)
            make_zip(start_n + n // 2, start_m, n //
                     2, arr, total_len, result_dict)
            make_zip(start_n, start_m + n // 2, n //
                     2, arr, total_len, result_dict)
            make_zip(start_n + n // 2, start_m + n // 2,
                     n // 2, arr, total_len, result_dict)
        return


def solution(arr):
    result_dict = {
        0: 0, 1: 0
    }
    total_len = len(arr)
    make_zip(0, 0, len(arr), arr, total_len, result_dict)
    return [result_dict[0], result_dict[1]]
