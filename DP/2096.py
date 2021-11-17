# 내려가기
N = int(input())
dp_max = [0, 0, 0]
dp_min = [0, 0, 0]
for i in range(N):
    a, b, c = map(int, input().split())
    max_a = max(a+dp_max[0], a+dp_max[1])
    max_b = max(b+dp_max[0], b+dp_max[1], b+dp_max[2])
    max_c = max(c+dp_max[1], c+dp_max[2])

    min_a = min(a+dp_min[0], a+dp_min[1])
    min_b = min(b+dp_min[0], b+dp_min[1], b+dp_min[2])
    min_c = min(c+dp_min[1], c+dp_min[2])
    dp_max = [max_a, max_b, max_c]
    dp_min = [min_a, min_b, min_c]
print(max(dp_max), min(dp_min))
