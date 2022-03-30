# 이차원 배열과 연산
from collections import defaultdict

def sorting(A):
    max_len = 0
    for i in range(len(A)):
        tmp_dict = defaultdict(int)
        for j in range(len(A[i])):
            if A[i][j]:
                tmp_dict[A[i][j]] += 1
        tmp_arr = sorted(list(tmp_dict.items()), key=lambda x: (x[1], x[0]))
        new_arr = []
        for a, b in tmp_arr:
            new_arr.append(a)
            new_arr.append(b)
        A[i] = new_arr
        max_len = max(max_len, len(A[i]))
    max_len = min(max_len, 100)
    for i in range(len(A)):
        if len(A[i]) < max_len:
            A[i] = A[i] + [0] * (max_len - len(A[i]))
        elif len(A[i]) > max_len:
            A[i] = A[i][:max_len]

r,c,k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
result = 0
while result <= 100:
    if r <= len(A) and c <= len(A[0]) and A[r-1][c-1] == k:
        break
    check_r = len(A)
    check_c = len(A[0])
    if check_r >= check_c:
        # 1-1. 행의 배열 정렬
        sorting(A)
    else:
        # 1-2. 열의 배열 정렬
        # 1-2-1. 열의 배열 정렬을 위한 임시 열의 리스트 생성
        tmp_A = []
        for i in range(len(A[0])):
            tmp_r = []
            for j in range(len(A)):
                tmp_r.append(A[j][i])
            tmp_A.append(tmp_r)

        sorting(tmp_A)

        return_tmp = [[] for _ in range(len(tmp_A[0]))]
        for i in range(len(tmp_A)):
            for j in range(len(tmp_A[i])):
                return_tmp[j].append(tmp_A[i][j])
        A = return_tmp
    result += 1
    
print(result if result <= 100 else -1)