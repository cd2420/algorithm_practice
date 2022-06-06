# 럭키스트레이트
n = list(input())
left = n[:len(n) // 2]
right = n[len(n) // 2:]
left_num = 0
for num in left:
    left_num += int(num)
right_num = 0
for num in right:
    right_num += int(num)
if left_num == right_num:
    print('LUCKY')
else :
    print('READY')