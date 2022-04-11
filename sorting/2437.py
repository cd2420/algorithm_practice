# 저울
n = int(input())
weights = list(map(int, input().split()))
weights.sort()
result = 0

for i in range(n):
    w = weights[i]
    if w - result > 1:
        result += 1
        break
    else :
        result += w
else :
    result += 1
print(result)
