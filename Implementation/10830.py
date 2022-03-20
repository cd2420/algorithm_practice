# 행렬 제곱
def arrMultiple(arr1, arr2):
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp[i][j] += arr1[i][k] * arr2[j][k]
            tmp[i][j] = tmp[i][j] % 1000
    return tmp


def makeArr2(arr):
    arr2 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr2[i][j] = arr[j][i]
    return arr2


n, b = map(int, input().split())
arr_1 = [list(map(int, input().split())) for _ in range(n)]
if b == 1:
    for arr in arr_1:
        for a in arr:
            print(a % 1000, end=" ")
        print()
else:
    rest_arr = []
    while b > 1:
        if b % 2 != 0:
            rest_arr.append(arr_1)
        arr_2 = makeArr2(arr_1)
        arr_1 = arrMultiple(arr_1, arr_2)
        b //= 2
    for _arr in rest_arr:
        arr_2 = makeArr2(_arr)
        arr_1 = arrMultiple(arr_1, arr_2)
    for arr in arr_1:
        for a in arr:
            print(a, end=" ")
        print()
