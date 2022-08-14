# 박스 채우기
l, w, h = map(int, input().split())
n = int(input())
cubes = [list(map(int, input().split())) for _ in range(n)]
prev = 0
result = 0
while cubes:
    a, b = cubes.pop()
    prev *= 8
    now = 2 ** a
    cnt_l = l // now
    cnt_w = w // now
    cnt_h = h // now
    cnt = cnt_l * cnt_w * cnt_h
    if cnt - prev > 0:
        plus_cnt = cnt - prev if cnt - prev <= b else b
        result += plus_cnt
        prev += plus_cnt
print(result if prev == l*w*h else -1)