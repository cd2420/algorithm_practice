# 안테나
n = int(input())
antena = list(map(int, input().split()))
antena.sort()
size = len(antena)
t = size // 2
total = 0
for a in antena:
    total += abs(a - antena[t])
result = antena[t]
if size % 2 == 0:
    t1 = t - 1
    check = 0
    for a in antena:
        check += abs(a - antena[t1])
    if total >= check:
        result = antena[t1]
print(result)