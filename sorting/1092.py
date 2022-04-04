# 배
n = int(input())
crain = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))
crain.sort(reverse=True)
boxes.sort()
if crain[0] < boxes[-1]:
    print(-1)
else :
    result = 0
    while boxes:
        for i in range(n):
            b_idx = len(boxes) - 1
            while b_idx >= 0:
                if crain[i] >= boxes[b_idx]:
                    box = boxes.pop(b_idx)
                    break
                else :
                    b_idx -= 1
        result += 1
    print(result)
