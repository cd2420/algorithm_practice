# 소용돌이 이쁘게 출력하기

def get_num(end, idx, r, c):
    count = 0
    if r == idx:
        count = idx - c
    elif c == -idx:
        count = idx*2 + idx - r
    elif r == -idx:
        count = idx*4 + idx + c
    elif c == idx:
        count = idx*6 + idx + r

    return end - count


r2, c2, r1, c1 = map(int, input().split())
result = []
for i in range(r2, r1 + 1, 1):
    row = []
    for j in range(c2, c1 + 1, 1):
        if 0 <= i and 0 <= j and i == j:
            row.append((2*i + 1) ** 2)
            continue
        t_i = abs(i)
        t_j = abs(j)
        idx = max(abs(t_i), abs(t_j)) 
        length = idx * 2 + 1
        end = length ** 2
        row.append(get_num(end, idx, i, j))
    result.append(row)

max_num = -1
for r in result:
    max_num = max(max_num, max(r))
max_num_len = len(str(max_num))
for r in result:
    for i in r:
        print(str(i).rjust(max_num_len), end=" ")
    print()