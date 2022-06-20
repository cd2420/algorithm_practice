# 경쟁적 전염
def is_ok(idx):
    if 0 <= idx < n*n and virus[idx] == 0: 
        return True
    else:
        return False

n,k = map(int, input().split())
virus = [0] * (n * n)
virus_idx = [[] for _ in range(k+1)]
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 0:
            continue
        virus[i*n + j] = arr[j]
        virus_idx[arr[j]].append(i*n + j)
s,x,y = map(int, input().split())

x -= 1
y -= 1

for _ in range(s):
    for i in range(1, k+1):
        append_list = []
        while virus_idx[i]:
            vidx = virus_idx[i].pop()
            if is_ok(vidx + 1):
                virus[vidx + 1] = i
                append_list.append(vidx + 1)
            if is_ok(vidx - 1):
                virus[vidx - 1] = i
                append_list.append(vidx - 1)
            if is_ok(vidx + n):
                virus[vidx + n] = i
                append_list.append(vidx + n)
            if is_ok(vidx - n):
                virus[vidx - n] = i
                append_list.append(vidx - n)
        virus_idx[i].extend(append_list)
print(virus[n * x + y])

