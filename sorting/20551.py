# Sort 마스터 배지훈의 후계자
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = sorted(A)
tree = {}
for i in range(len(B)):
    check = str(B[i])
    if check not in tree:
        tree[check] = i
    else :
        tree[check] = min(tree[check], i)

for _ in range(M):
    check = input().rstrip()
    if check not in tree:
        print(-1)
    else :
        print(tree[check])

